<?php

// simple PHP 

require_once 'common.php';

// Load the POST.
$post = file_get_contents("php://input");
$data = json_decode($post, true);

//echo "data";

$dbh = openDb();

//if ($dbh != null) {
// echo "db connection success";
//} else {
// echo "db connection fail";
//}

if ($data["opr"] == "w") {
  $sth = $dbh->prepare("INSERT INTO BoundingBoxes (ID, Time, Line) SELECT COUNT(*)+1, NOW(), :line FROM BoundingBoxes");
  $sth->bindParam(':line', $data["Line"], PDO::PARAM_INT);
  $ret = $sth->execute();
}

if (empty($data["time"])) {
    $sth = $dbh->prepare("SELECT * from BoundingBoxes ORDER BY Time DESC LIMIT 10");
} else {
    $sth =$dbh->prepare("SELECT * from BoundingBoxes ORDER BY ABS(TIMEDIFF(:time Time)) LIMIT 10");
    $sth->bindParam(':time', $data["Time"], PDO::PARAM_STR);
}
$ret = $sth->execute();
$rd = $sth->fetchAll();

//print_r($rd);

$json_value = null;
$records = array();

foreach($rd as $key => $value) {
    array_push($records,
    array(
        'Line' => (int)$value["Line"],
        'Time' =>$value["Time"],
        'ID' =>$value["ID"])
    );
}

$json_value = json_encode($records);

header('Content-Type: text/javascript; charset=utf-8');

echo $json_value;

?>


