using MySQL

con = mysql_connect("mysql-amigo.ebi.ac.uk", "go_select", " amigo", "go_latest")

command = "SELECT * FROM term WHERE acc='GO:0005634';"

mysql_execute(con, command)