module main {
    requires javafx.controls;
    requires javafx.fxml;
    requires java.sql;
    requires javafx.swing;


    opens main to javafx.fxml;
    exports main;
    exports main.piechart;
    opens main.piechart to javafx.fxml;
    exports main.barchart;
    opens main.barchart to javafx.fxml;
    exports main.linechart;
    opens main.linechart to javafx.fxml;
}