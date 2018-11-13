package io.improbable.keanu.vertices.dbl.nonprobabilistic;

import io.improbable.keanu.annotation.ExportVertexToPythonBindings;
import io.improbable.keanu.tensor.NumberTensor;
import io.improbable.keanu.tensor.dbl.DoubleTensor;
import io.improbable.keanu.vertices.*;
import io.improbable.keanu.vertices.dbl.DoubleVertex;
import io.improbable.keanu.vertices.dbl.KeanuRandom;

public class CastDoubleVertex extends DoubleVertex implements SaveableVertex, NonProbabilistic<DoubleTensor> {

    private final Vertex<? extends NumberTensor> inputVertex;
    private static final String INPUT_VERTEX_NAME = "inputvertex";

    @ExportVertexToPythonBindings
    public CastDoubleVertex(@LoadParentVertex(INPUT_VERTEX_NAME) Vertex<? extends NumberTensor> inputVertex) {
        super(inputVertex.getShape());
        this.inputVertex = inputVertex;
        setParents(inputVertex);
    }

    @SaveParentVertex(INPUT_VERTEX_NAME)
    public Vertex<? extends NumberTensor> getInputVertex() {
        return inputVertex;
    }

    @Override
    public DoubleTensor sample(KeanuRandom random) {
        return inputVertex.sample(random).toDouble();
    }

    @Override
    public DoubleTensor calculate() {
        return inputVertex.getValue().toDouble();
    }
}
