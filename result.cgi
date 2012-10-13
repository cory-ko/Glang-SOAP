#!/usr/bin/env perl
use strict;
use warnings;
use CGI;

my $cgi = CGI->new;
my $jobid = $cgi->param('jobid');

my $baseUrl = 'http://soap.g-language.org/WS/';

unless ( $jobid ) {
    print <<HTML;
Status: 404
Content-type: text/html

<!DOCTYPE HTML PUBLIC "-//IETF//DTD HTML 2.0//EN">
<html><head>
<title>404 Not Found</title>
</head><body>
<h1>Job ID is not Found</h1>
<p>The JobID $jobid was not found on this server.</p>
HTML
    exit();
}

if (-e "./graph/$jobid.png") {
    print "Location: $baseUrl/graph/$jobid.png\n\n";
} elsif (-e "./data/$jobid.csv") {
    print "Location: $baseUrl/data/$jobid.csv\n\n";
} elsif (-e "./data/$jobid.gbk") {
    print "Location: $baseUrl/data/$jobid.gbk\n\n";
} else {
    print <<HTML;
Status: 404
Content-type: text/html

<!DOCTYPE HTML PUBLIC "-//IETF//DTD HTML 2.0//EN">
<html><head>
<title>404 Not Found</title>
</head><body>
<h1>Result not Found</h1>
<p>Your Job ID $jobid was not found on this server.</p>
HTML
}
