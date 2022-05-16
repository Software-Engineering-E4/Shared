package apps;

import database.Database;
import stanford.NLP;
import tools.Tool;
import java.sql.*;
import java.util.List;

public class Twitter {

    private Twitter(){}

    private static void updatePost(String id, String sentiment){

        Connection con = Database.getConnection();
        try {
            PreparedStatement statement = con.prepareStatement("UPDATE twitter_posts SET sentiment = ? WHERE id = ?");
            statement.setString(1, sentiment);
            statement.setString(2, id);
            System.out.println(statement);
            statement.executeUpdate();
            statement.close();
        }catch (SQLException e){
            e.printStackTrace();
        }
    }

    public static void analyzePosts(){

        Connection con = Database.getConnection();
        try {
            Statement stmt = con.createStatement();
            ResultSet rs = stmt.executeQuery(" SELECT * FROM twitter_posts WHERE sentiment is NULL");

            while (rs.next()) {
                String id = rs.getString("id");
                String text = rs.getString("text");

                List<Double> sentimentList = NLP.estimatingSentiment(text);  // poz 0 - % negative sentiment | poz 1 - % neutral sentiment | poz 2 - % positive sentiment
                Tool.format(sentimentList);
                String sentiment = Tool.predominantSentiment(sentimentList);
                updatePost(id, sentiment);
            }
            rs.close();
            stmt.close();
        } catch (SQLException e){
            e.printStackTrace();
        }
    }

}