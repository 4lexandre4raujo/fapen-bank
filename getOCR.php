<?php
header("Access-Control-Allow-Origin: *");
    
    putenv('LANG=en_US.UTF-8');
    $arg = $_GET['url'];
    $output = shell_exec('python defOCR.py "'.$arg.'"');
    $output = str_replace('"', '', $output);
    $output = str_replace('[', '', $output);
    $output = str_replace('[', ']', $output);
    $output = str_replace("'", "", $output);
    $output = str_replace(" ", "", $output);
    $result = json_encode($output);
    // $command = escapeshellcmd('python defOCR.py');
    // $output = shell_exec($command);
    echo $output;
?>