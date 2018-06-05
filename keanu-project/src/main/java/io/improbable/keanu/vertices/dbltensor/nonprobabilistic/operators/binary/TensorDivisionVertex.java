package io.improbable.keanu.vertices.dbltensor.nonprobabilistic.operators.binary;

import io.improbable.keanu.tensor.dbl.DoubleTensor;
import io.improbable.keanu.vertices.Vertex;
import io.improbable.keanu.vertices.dbltensor.DoubleTensorVertex;
import io.improbable.keanu.vertices.dbltensor.nonprobabilistic.diff.TensorDualNumber;

import java.util.Map;

import static io.improbable.keanu.tensor.TensorShapeValidation.checkHasSingleNonScalarShapeOrAllScalar;

public class TensorDivisionVertex extends TensorDoubleBinaryOpVertex {

    public TensorDivisionVertex(DoubleTensorVertex a, DoubleTensorVertex b) {
        super(checkHasSingleNonScalarShapeOrAllScalar(a.getShape(), b.getShape()), a, b);
    }

    @Override
    public TensorDualNumber calculateDualNumber(Map<Vertex, TensorDualNumber> dualNumbers) {
        TensorDualNumber aDual = dualNumbers.get(a);
        TensorDualNumber bDual = dualNumbers.get(b);
        return aDual.divideBy(bDual);
    }

    @Override
    protected DoubleTensor op(DoubleTensor a, DoubleTensor b) {
        return a.div(b);
    }
}
