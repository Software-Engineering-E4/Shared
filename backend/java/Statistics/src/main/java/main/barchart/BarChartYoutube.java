package main.barchart;


import javafx.collections.FXCollections;
import javafx.scene.chart.BarChart;
import javafx.scene.chart.CategoryAxis;
import javafx.scene.chart.NumberAxis;
import javafx.scene.chart.XYChart;
import youtube.YoutubeVideo;

import java.sql.SQLException;
import java.util.Arrays;
import java.util.List;

public class BarChartYoutube  {

    public static BarChart<String,Number> barChartYoutube() throws SQLException {

        YoutubeVideo youtubeVideo = new YoutubeVideo();

        Double[] neutral = new Double[9];
        Double[] negative = new Double[9];
        Double[] positive = new Double[9];
        List<String> months = Arrays.asList("01", "04", "05", "08", "09", "12");

        int i = 0;
        int year;
        for (year = 2020; year <= 2022; year++) {
            neutral[i] = youtubeVideo.findNeutralPostByMonthAndYear(months.get(0), months.get(1), year);
            negative[i] = youtubeVideo.findNegativePostByMonthAndYear(months.get(0), months.get(1), year);
            positive[i] = youtubeVideo.findPositivePostByMonthAndYear(months.get(0), months.get(1), year);

            neutral[i + 1] = youtubeVideo.findNeutralPostByMonthAndYear(months.get(2), months.get(3), year);
            negative[i + 1] = youtubeVideo.findNegativePostByMonthAndYear(months.get(2), months.get(3), year);
            positive[i + 1] = youtubeVideo.findPositivePostByMonthAndYear(months.get(2), months.get(3), year);

            neutral[i + 2] = youtubeVideo.findNeutralPostByMonthAndYear(months.get(4), months.get(5), year);
            negative[i + 2] = youtubeVideo.findNegativePostByMonthAndYear(months.get(4), months.get(5), year);
            positive[i + 2] = youtubeVideo.findPositivePostByMonthAndYear(months.get(4), months.get(5), year);
            i += 3;

        }


        CategoryAxis xAxis = new CategoryAxis();

        xAxis.setCategories(FXCollections.observableArrayList(Arrays.asList(
                "Jan-Apr 2020", "May-Aug 2020", "Sept-Dec 2020", "Jan-Apr 2021", "May-Aug 2021", "Sept-Dec 2021", "Jan-Apr 2022", "May-Aug 2022")));
        xAxis.setLabel("Month-Year");


        NumberAxis yAxis = new NumberAxis();
        yAxis.setLabel("Score");

        BarChart<String, Number> barChart = new BarChart<>(xAxis, yAxis);
        barChart.setTitle("Comparison between videos over the years");

        XYChart.Series<String, Number> series1 = new XYChart.Series<>();
        series1.setName("Negative");
        series1.getData().add(new XYChart.Data<>("Jan-Apr 2020", negative[0]));
        series1.getData().add(new XYChart.Data<>("May-Aug 2020", negative[1]));
        series1.getData().add(new XYChart.Data<>("Sept-Dec 2020", negative[2]));
        series1.getData().add(new XYChart.Data<>("Jan-Apr 2021", negative[3]));
        series1.getData().add(new XYChart.Data<>("May-Aug 2021", negative[4]));
        series1.getData().add(new XYChart.Data<>("Sept-Dec 2021", negative[5]));
        series1.getData().add(new XYChart.Data<>("Jan-Apr 2022", negative[6]));
        series1.getData().add(new XYChart.Data<>("May-Aug 2022", negative[7]));


        XYChart.Series<String, Number> series2 = new XYChart.Series<>();
        series2.setName("Neutral");
        series2.getData().add(new XYChart.Data<>("Jan-Apr 2020", neutral[0]));
        series2.getData().add(new XYChart.Data<>("May-Aug 2020", neutral[1]));
        series2.getData().add(new XYChart.Data<>("Sept-Dec 2020", neutral[2]));
        series2.getData().add(new XYChart.Data<>("Jan-Apr 2021", neutral[3]));
        series2.getData().add(new XYChart.Data<>("May-Aug 2021", neutral[4]));
        series2.getData().add(new XYChart.Data<>("Sept-Dec 2021", neutral[5]));
        series2.getData().add(new XYChart.Data<>("Jan-Apr 2022", neutral[6]));
        series2.getData().add(new XYChart.Data<>("May-Aug 2022", neutral[7]));


        XYChart.Series<String, Number> series3 = new XYChart.Series<>();
        series3.setName("Positive");
        series3.getData().add(new XYChart.Data<>("Jan-Apr 2020", positive[0]));
        series3.getData().add(new XYChart.Data<>("May-Aug 2020", positive[1]));
        series3.getData().add(new XYChart.Data<>("Sept-Dec 2020", positive[2]));
        series3.getData().add(new XYChart.Data<>("Jan-Apr 2021", positive[3]));
        series3.getData().add(new XYChart.Data<>("May-Aug 2021", positive[4]));
        series3.getData().add(new XYChart.Data<>("Sept-Dec 2021", positive[5]));
        series3.getData().add(new XYChart.Data<>("Jan-Apr 2022", positive[6]));
        series3.getData().add(new XYChart.Data<>("May-Aug 2022", positive[7]));


        barChart.getData().addAll(series1, series2, series3);
        barChart.setBarGap(1);
        barChart.setCategoryGap(4);
        barChart.setMaxHeight(600);
        barChart.setMinHeight(600);
        barChart.setMinWidth(800);
        barChart.setMaxWidth(800);

        return barChart;
    }

}
