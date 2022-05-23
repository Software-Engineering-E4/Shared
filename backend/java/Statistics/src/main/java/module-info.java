module com.example.statist {
    requires javafx.controls;
    requires javafx.fxml;
    requires java.sql;
    requires java.desktop;
    requires javafx.swing;


    opens com.example.statist to javafx.fxml;
    exports main;
}