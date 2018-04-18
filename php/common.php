<?php

function openDb() {
  $dsn = 'mysql:host=localhost;dbname=rsiot05;charset=utf8';
  $username = 'rsiot05';
  $password = 'iort695';
  //echo $password;
  $options = array(
    PDO::MYSQL_ATTR_INIT_COMMAND => 'SET NAMES utf8',
    );

  try {
    $dbh = new PDO($dsn, $username, $password, $options);
    $dbh->setAttribute(PDO::ATTR_STRINGIFY_FETCHES, false);
    $sth = $dbh->prepare("SELECT @@session.time_zone, SET time_zone='-05:00'");
    $sth->execute();
  } catch (PDOException $e) {
    return null;
  }
  return $dbh;
}

?>