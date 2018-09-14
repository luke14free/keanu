package io.improbable.keanu.tensor.validate;

import io.improbable.keanu.tensor.bool.BooleanTensor;
import io.improbable.keanu.tensor.dbl.DoubleTensor;

public class ChangeValueTo implements TensorValidationPolicy {
    private final double value;

    public ChangeValueTo(double value) {
        this.value = value;
    }

    @Override
    public DoubleTensor handle(DoubleTensor tensor, BooleanTensor result) {
        return tensor.setWithMask(result.toDoubleMask(), value);
    }
}
