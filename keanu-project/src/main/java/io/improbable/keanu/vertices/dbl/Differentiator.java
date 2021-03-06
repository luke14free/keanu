package io.improbable.keanu.vertices.dbl;

import io.improbable.keanu.vertices.Vertex;
import io.improbable.keanu.vertices.VertexId;
import io.improbable.keanu.vertices.dbl.nonprobabilistic.diff.PartialDerivative;
import io.improbable.keanu.vertices.dbl.nonprobabilistic.diff.PartialsOf;
import io.improbable.keanu.vertices.dbl.nonprobabilistic.diff.PartialsWithRespectTo;
import lombok.experimental.UtilityClass;

import java.util.Arrays;
import java.util.Collection;
import java.util.Collections;
import java.util.Comparator;
import java.util.HashMap;
import java.util.HashSet;
import java.util.Map;
import java.util.PriorityQueue;
import java.util.Set;


@UtilityClass
public class Differentiator {

    public static <V extends Vertex & Differentiable> PartialsWithRespectTo forwardModeAutoDiff(V wrt, V... of) {
        return forwardModeAutoDiff(wrt, new HashSet<>(Arrays.asList(of)));
    }

    public static <V extends Vertex & Differentiable> PartialsWithRespectTo forwardModeAutoDiff(V wrt, Collection<V> of) {

        PriorityQueue<V> priorityQueue = new PriorityQueue<>(Comparator.comparing(Vertex::getId, Comparator.naturalOrder()));
        priorityQueue.add(wrt);

        HashSet<Vertex> alreadyQueued = new HashSet<>();
        alreadyQueued.add(wrt);

        Map<Vertex, PartialDerivative> partials = new HashMap<>();
        Map<VertexId, PartialDerivative> ofWrt = new HashMap<>();

        while (!priorityQueue.isEmpty()) {
            V visiting = priorityQueue.poll();

            PartialDerivative partialOfVisiting = visiting.forwardModeAutoDifferentiation(partials);
            partials.put(visiting, partialOfVisiting);

            if (of.contains(visiting)) {
                ofWrt.put(visiting.getId(), partialOfVisiting);
                continue;
            }

            for (Vertex child : (Set<Vertex<?>>) visiting.getChildren()) {
                if (!child.isProbabilistic() && !alreadyQueued.contains(child) && child instanceof Differentiable) {
                    priorityQueue.offer((V) child);
                    alreadyQueued.add(child);
                }
            }
        }

        return new PartialsWithRespectTo(wrt, ofWrt);
    }

    public static PartialsOf reverseModeAutoDiff(Vertex ofVertex, Set<DoubleVertex> wrt) {
        if (ofVertex.isObserved()) {
            return new PartialsOf(ofVertex, Collections.emptyMap());
        } else {
            return reverseModeAutoDiff(ofVertex, Differentiable.withRespectToSelf(ofVertex.getShape()), wrt);
        }
    }

    public static PartialsOf reverseModeAutoDiff(Vertex ofVertex, DoubleVertex... wrt) {
        return reverseModeAutoDiff(ofVertex, new HashSet<>(Arrays.asList(wrt)));
    }

    public static PartialsOf reverseModeAutoDiff(Vertex<?> ofVertex, PartialDerivative dWrtOfVertex, Set<? extends Vertex<?>> wrt) {

        ensureGraphValuesAndShapesAreSet(ofVertex);

        PriorityQueue<Vertex> priorityQueue = new PriorityQueue<>(Comparator.<Vertex, VertexId>comparing(Vertex::getId, Comparator.naturalOrder()).reversed());
        priorityQueue.add(ofVertex);

        HashSet<Vertex> alreadyQueued = new HashSet<>();
        alreadyQueued.add(ofVertex);

        Map<Vertex, PartialDerivative> dwrtOf = new HashMap<>();
        dwrtOf.put(ofVertex, dWrtOfVertex);

        Map<VertexId, PartialDerivative> wrtOf = new HashMap<>();

        Vertex<?> visiting;
        while ((visiting = priorityQueue.poll()) != null) {

            if (wrt.contains(visiting)) {
                wrtOf.put(visiting.getId(), dwrtOf.get(visiting));
                continue;
            }

            if (!visiting.isProbabilistic()) {

                if (visiting instanceof Differentiable) {

                    Differentiable visitingDifferentiable = ((Differentiable) visiting);
                    PartialDerivative derivativeOfOutputWrtVisiting = dwrtOf.get(visiting);

                    if (derivativeOfOutputWrtVisiting != null) {

                        Map<Vertex, PartialDerivative> partialDerivatives = visitingDifferentiable.reverseModeAutoDifferentiation(derivativeOfOutputWrtVisiting);
                        collectPartials(partialDerivatives, dwrtOf);

                        for (Vertex parent : visiting.getParents()) {
                            if (!alreadyQueued.contains(parent) && parent instanceof Differentiable) {
                                priorityQueue.offer(parent);
                                alreadyQueued.add(parent);
                            }
                        }

                    }
                }

            }
        }

        return new PartialsOf(ofVertex, wrtOf);
    }

    private static void ensureGraphValuesAndShapesAreSet(Vertex<?> vertex) {
        vertex.getValue();
    }

    private static void collectPartials(Map<Vertex, PartialDerivative> partialDerivatives,
                                        Map<Vertex, PartialDerivative> dwrtOf) {

        for (Map.Entry<Vertex, PartialDerivative> v : partialDerivatives.entrySet()) {

            Vertex wrtVertex = v.getKey();
            PartialDerivative dwrtV = v.getValue();

            if (dwrtOf.containsKey(wrtVertex)) {
                dwrtOf.put(wrtVertex, dwrtOf.get(wrtVertex).add(dwrtV));
            } else {
                dwrtOf.put(wrtVertex, dwrtV);
            }
        }
    }
}
