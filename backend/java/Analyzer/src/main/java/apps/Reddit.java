package apps;

import database.Database;
import stanford.NLP;
import tools.Tool;

import java.sql.*;
import java.util.List;

public class Reddit {

    private Reddit(){}

    private static void updateComm(String id, String sentiment){

        Connection con = Database.getConnection();
        try {
            PreparedStatement statement = con.prepareStatement("UPDATE reddit_comments SET sentiment = ? WHERE id = ?");
            statement.setString(1, sentiment);
            statement.setString(2, id);
            System.out.println(statement);
            statement.executeUpdate();
            statement.close();
        } catch (SQLException e){
            e.printStackTrace();
        }
    }

    private static void updatePost(String id, Double negative, Double neutral, Double positive){

        Connection con = Database.getConnection();
        try {
            PreparedStatement statement = con.prepareStatement("UPDATE reddit_posts SET negative = ?, neutral = ?, positive = ? WHERE id = ?");
            statement.setDouble(1, negative);
            statement.setDouble(2, neutral);
            statement.setDouble(3, positive);
            statement.setString(4, id);
            System.out.println(statement);
            statement.executeUpdate();
            statement.close();
        } catch (SQLException e){
            e.printStackTrace();
        }
    }

    public static void analyzeComments(){

        try{
            Connection con = Database.getConnection();
            ResultSet rs = con.createStatement().executeQuery(" SELECT * FROM reddit_comments where sentiment IS NULL");

            while( rs.next() ){
                String id = rs.getString("id");
                String selfText = rs.getString("selftext");

                List<Double> sentimentList = NLP.estimatingSentiment(selfText);  // poz 0 - % negative sentiment | poz 1 - % neutral sentiment | poz 2 - % positive sentiment
                Tool.format(sentimentList);
                String sentiment = Tool.predominantSentiment(sentimentList);
                updateComm(id, sentiment);
            }
            rs.close();
        } catch (SQLException e){
            e.printStackTrace();
        }
    }

    public static void analyzePosts(){

        try {
            Connection con = Database.getConnection();
            Statement stmt = con.createStatement();
            ResultSet rs = stmt.executeQuery(" SELECT * FROM reddit_posts where neutral IS NULL");

            while (rs.next()) {
                String id = rs.getString("id");
                String selfText = rs.getString("selftext");
                String title = rs.getString("title");

                System.out.println(id);

                if( selfText == null )
                    selfText = title;
                else
                    selfText = title.concat(". ").concat(selfText);

                List<Double> sentimentList = NLP.estimatingSentiment(selfText);  // poz 0 - % negative sentiment | poz 1 - % neutral sentiment | poz 2 - % positive sentiment
                Tool.format(sentimentList);
                updatePost(id, sentimentList.get(0), sentimentList.get(1), sentimentList.get(2));
            }
            rs.close();
            stmt.close();
        } catch (SQLException e){
            e.printStackTrace();
        }
    }

}