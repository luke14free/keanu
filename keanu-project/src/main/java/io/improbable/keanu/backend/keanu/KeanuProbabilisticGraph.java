package io.improbable.keanu.backend.keanu;

import io.improbable.keanu.algorithms.graphtraversal.VertexValuePropagation;
import io.improbable.keanu.backend.LogProbWithSample;
import io.improbable.keanu.backend.ProbabilisticGraph;
import io.improbable.keanu.network.BayesianNetwork;
import io.improbable.keanu.vertices.Vertex;
import io.improbable.keanu.vertices.VertexLabel;
import lombok.Getter;

import java.util.ArrayList;
import java.util.List;
import java.util.Map;
import java.util.stream.Collectors;

import static java.util.stream.Collectors.toMap;

public class KeanuProbabilisticGraph implements ProbabilisticGraph {

    @Getter
    private final BayesianNetwork bayesianNetwork;

    @Getter
    private final Map<VertexLabel, Vertex> vertexLookup;

    public KeanuProbabilisticGraph(BayesianNetwork bayesianNetwork) {
        this.bayesianNetwork = bayesianNetwork;
        this.vertexLookup = bayesianNetwork.getLatentVertices().stream()
            .filter(v -> v.getLabel() != null)
            .collect(toMap(Vertex::getLabel, v -> v));
    }

    @Override
    public double logProb(Map<String, ?> inputs) {
        cascadeUpdate(inputs);
        return this.bayesianNetwork.getLogOfMasterP();
    }

    @Override
    public LogProbWithSample logProbWithSample(Map<String, ?> inputs, List<String> outputs) {

        double logProb = logProb(inputs);
        Map<String, ?> sample = outputs.stream().collect(Collectors.toMap(
            output -> output,
            output -> vertexLookup.get(new VertexLabel(output)).getValue()
        ));

        return new LogProbWithSample(logProb, sample);
    }

    public void cascadeUpdate(Map<String, ?> inputs) {

        List<Vertex> updatedVertices = new ArrayList<>();
        for (Map.Entry<String, ?> input : inputs.entrySet()) {
            Vertex updatingVertex = vertexLookup.get(new VertexLabel(input.getKey()));
            updatingVertex.setValue(input.getValue());
            updatedVertices.add(updatingVertex);
        }

        VertexValuePropagation.cascadeUpdate(updatedVertices);
    }

}