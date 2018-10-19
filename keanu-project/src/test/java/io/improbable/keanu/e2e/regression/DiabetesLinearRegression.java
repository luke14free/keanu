package io.improbable.keanu.e2e.regression;

import static org.hamcrest.MatcherAssert.assertThat;
import static org.hamcrest.Matchers.greaterThan;
import static org.junit.Assert.assertEquals;

import java.util.List;

import io.improbable.keanu.model.regression.RegressionRegularization;
import io.improbable.keanu.util.CsvDataResource;
import org.junit.Rule;
import org.junit.Test;

import io.improbable.keanu.algorithms.variational.optimizer.gradient.GradientOptimizer;
import io.improbable.keanu.model.ModelScoring;
import io.improbable.keanu.model.regression.RegressionModel;
import io.improbable.keanu.network.BayesianNetwork;
import io.improbable.keanu.tensor.dbl.DoubleTensor;
import io.improbable.keanu.vertices.ConstantVertex;
import io.improbable.keanu.vertices.dbl.DoubleVertex;
import io.improbable.keanu.vertices.dbl.probabilistic.GaussianVertex;

/**
 * This data set was taken from https://www4.stat.ncsu.edu/~boos/var.select/diabetes.html
 * It's also the same data set used for scikitlearn load_diabetes at
 * http://scikit-learn.org/stable/auto_examples/linear_model/plot_ols.html
 */
public class DiabetesLinearRegression {
    @Rule
    public CsvDataResource<Data> csvDataResource = new CsvDataResource<>("data/datasets/diabetes/diabetes_standardized_training.csv", Data.class);

    @Test
    public void doesLinearRegressionOnBMI() {
        Data data = csvDataResource.getData();

        // Linear Regression
        DoubleVertex weight = new GaussianVertex(0.0, 100);
        DoubleVertex b = new GaussianVertex(0.0, 100);
        DoubleVertex x = ConstantVertex.of(data.bmi);
        DoubleVertex yMu = x.multiply(weight);

        DoubleVertex y = new GaussianVertex(yMu.plus(b), 1.0);
        y.observe(data.y);

        BayesianNetwork bayesNet = new BayesianNetwork(y.getConnectedGraph());
        GradientOptimizer optimizer = GradientOptimizer.of(bayesNet);
        optimizer.maxLikelihood();

        assertEquals(938.2378, weight.getValue().scalar(), 0.01);
        assertEquals(152.9189, b.getValue().scalar(), 0.01);
    }

    @Test
    public void doesLinearRegressionOnBMIAsModel() {
        Data data = csvDataResource.getData();

        RegressionModel linearRegressionModel = RegressionModel.withTrainingData(data.bmi, data.y)
            .setRegularization(RegressionRegularization.RIDGE)
            .setPriorOnWeightsAndIntercept(0, 100)
            .build();
        assertEquals(938.2378, linearRegressionModel.getWeight(0), 0.5);
        assertEquals(152.9189, linearRegressionModel.getIntercept(), 0.5);
    }

    @Test
    public void canPredictFutureValuesWithLinearRegression() {
        Data data = csvDataResource.getData();

        int sizeOfTestData = 100;

        List<DoubleTensor> splitXData = data.bmi.split(1, (int) data.bmi.getLength() - sizeOfTestData, (int) data.bmi.getLength() - 1);
        DoubleTensor xTrainingData = splitXData.get(0);
        DoubleTensor xTestData = splitXData.get(1);

        List<DoubleTensor> splitYData = data.y.split(1, (int) data.y.getLength() - sizeOfTestData, (int) data.bmi.getLength() - 1);
        DoubleTensor yTrainingData = splitYData.get(0);
        DoubleTensor yTestData = splitYData.get(1);

        RegressionModel<DoubleTensor> linearRegressionModel = RegressionModel.withTrainingData(xTrainingData, yTrainingData)
            .build();

        double accuracyOnTestData = ModelScoring.coefficientOfDetermination(linearRegressionModel.predict(xTestData), yTestData);
        assertThat(accuracyOnTestData, greaterThan(0.3));
    }

    public static class Data {
        public DoubleTensor bmi;
        public DoubleTensor y;
    }

}
