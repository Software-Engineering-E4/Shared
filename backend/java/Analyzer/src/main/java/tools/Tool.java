package tools;

import java.util.Formatter;
import java.util.List;

public class Tool {

    private Tool(){}

    public static void format(List<Double> sentimentList){

        Formatter format = new Formatter();
        format.format("%.2f", sentimentList.get(0));
        sentimentList.set(0, Double.parseDouble(format.toString()));

        format = new Formatter();
        format.format("%.2f", sentimentList.get(1));
        sentimentList.set(1, Double.parseDouble(format.toString()));

        format = new Formatter();
        format.format("%.2f", sentimentList.get(2));
        sentimentList.set(2, Double.parseDouble(format.toString()));
    }

    public static String predominantSentiment(List<Double> sentimentList){

        String sentiment = "negative";
        double predominant = sentimentList.get(0);

        if( sentimentList.get(0) < sentimentList.get(1) ){
            predominant = sentimentList.get(1);
            sentiment = "neutral";
        }
        if( predominant < sentimentList.get(2) ){
            sentiment = "positive";
        }

        return sentiment;
    }

    public static String selectText(String description, String descriptionTranslated, String title, String titleTranslated){

        String toAnalyze = "";
        if( titleTranslated != null )
            toAnalyze = toAnalyze.concat(titleTranslated);
        else if( title != null)
            toAnalyze = toAnalyze.concat(title);

        if( descriptionTranslated != null )
            toAnalyze = toAnalyze.concat(descriptionTranslated);
        else if( description != null)
            toAnalyze = toAnalyze.concat(description);

        return toAnalyze;
    }
}