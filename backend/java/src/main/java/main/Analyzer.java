package main;
import apps.*;
import database.Database;
import stanford.NLP;

public class Analyzer {

    public static void main(String[] args) {

        NLP.init();
        Database.createConnection();

        Reddit.analyzePosts();
        Reddit.analyzeComments();

        YouTube.analyzePosts();
        YouTube.analyzeComm();

        Twitter.analyzePosts();

        Database.closeConnection();
    }
}