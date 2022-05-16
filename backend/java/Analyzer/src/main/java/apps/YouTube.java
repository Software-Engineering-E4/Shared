package apps;

import database.Database;
import stanford.NLP;
import tools.Tool;
import java.sql.*;
import java.util.ArrayList;
import java.util.List;

public class YouTube {

    private YouTube(){}

    private static void updatePost(String id, String sentiment){

        Connection con = Database.getConnection();

        try{
            PreparedStatement statement = con.prepareStatement("UPDATE youtube_videos SET sentiment = ? WHERE id = ?");
            statement.setString(1,sentiment);
            statement.setString(2,id);

            System.out.println(statement);
            statement.executeUpdate();
            statement.close();
        } catch (SQLException e){
            e.printStackTrace();
        }
    }

    private static void updateComm(String id, String sentiment){

        Connection con = Database.getConnection();

        try{
            PreparedStatement statement = con.prepareStatement("UPDATE youtube_comments SET sentiment = ? WHERE id = ?");
            statement.setString(1,sentiment);
            statement.setString(2,id);

            System.out.println(statement);
            statement.executeUpdate();
            statement.close();
        } catch(SQLException e){
            e.printStackTrace();
        }
    }

    public static void analyzePosts(){

        Connection con = Database.getConnection();
        try {
            ResultSet rs = con.createStatement().executeQuery(" SELECT * FROM youtube_videos WHERE sentiment is NULL");

            while (rs.next()) {
                String id = rs.getString("id");
                String description = rs.getString("description");
                String title = rs.getString("title");
                String descriptionTranslated = rs.getString("description");
                String titleTranslated = rs.getString("title_translated");

                System.out.println(id);
                String toAnalyze = Tool.selectText(description, descriptionTranslated, title, titleTranslated);

                List<Double> sentimentList = NLP.estimatingSentiment(toAnalyze);  // poz 0 - % negative sentiment | poz 1 - % neutral sentiment | poz 2 - % positive sentiment
                Tool.format(sentimentList);
                String sentiment = Tool.predominantSentiment(sentimentList);
                updatePost(id, sentiment);
            }
            rs.close();
        } catch (SQLException e){
            e.printStackTrace();
        }
    }

    public static void analyzeComm(){

        Connection con = Database.getConnection();
        try{
            ResultSet rs = con.createStatement().executeQuery("SELECT * FROM youtube_comments WHERE sentiment IS NULL");

            while(rs.next()){
                String id = rs.getString("id");
                String text = rs.getString("text");
                String translated = rs.getString("text_translated");

                System.out.println(id);
                List<Double> sentimentList = new ArrayList<>();

                if( !(translated == null && text == null) ) {

                    if (translated != null)
                        sentimentList = NLP.estimatingSentiment(translated);
                    else
                        sentimentList = NLP.estimatingSentiment(text);

                    Tool.format(sentimentList);
                    String sentiment = Tool.predominantSentiment(sentimentList);
                    updateComm(id, sentiment);
                }
            }
            rs.close();
        } catch (SQLException e){
            e.printStackTrace();
        }
    }

}