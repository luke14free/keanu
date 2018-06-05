package io.improbable.keanu.vertices.booltensor.nonprobabilistic.operators.binary.compare;

import io.improbable.keanu.tensor.NumberTensor;
import io.improbable.keanu.tensor.bool.BooleanTensor;
import io.improbable.keanu.vertices.Vertex;
import io.improbable.keanu.vertices.booltensor.nonprobabilistic.operators.binary.BoolBinaryOpVertex;

import static io.improbable.keanu.tensor.TensorShapeValidation.checkHasSingleNonScalarShapeOrAllScalar;

public class GreaterThanOrEqualVertex<A extends NumberTensor, B extends NumberTensor> extends BoolBinaryOpVertex<A, B> {

    public GreaterThanOrEqualVertex(Vertex<A> a, Vertex<B> b) {
        super(checkHasSingleNonScalarShapeOrAllScalar(a.getShape(), b.getShape()), a, b);
    }

    /**
     * Returns true if a is greater than or equal to b
     */
    @Override
    public BooleanTensor op(A a, B b) {
        return a.toDouble().greaterThanOrEqual(b.toDouble());
    }

}
