#!/usr/bin/env perl
use SOAP::Transport::HTTP;

SOAP::Transport::HTTP::CGI->dispatch_to('GLANG')->handle();

package GLANG;
use G;

use G::DB::SDB qw/ sdb_save _set_sdb_path /;
use G::IO;

sub codon_mva {
    my $self = shift;
    my $in0 = shift;

    my %param = %{+shift};

    for ( keys %param ) {
        if ($param{$_} eq "") {delete $param{$_};}
        else {$param{"-$_"} = $param{$_};}
    }

    _set_sdb_path("/tmp/gb");

    G::Messenger::msg_interface("Inspire");
    my ($trpData,$trpError);
    G::Messenger::msg_term_console(sub{$trpData .= shift @_ });
    G::Messenger::msg_system_console(sub{$trpError .= shift @_ });

    my $jobid = time.substr(rand(10),-4);
    while (-e "./graph/".$jobid.".png" || -e "./data/".$jobid.".csv") {
        $jobid = time.substr(rand(10),-4);
    }

    if ($in0 ne "ecoli" && $in0 ne "bsub" && $in0 ne "mgen" && $in0 ne "cyano" && $in0 ne "pyro") {
        my $tmpfile = ( (time % 1296000)*10 + int(rand(10)) + 1048576);
        if (substr($in0,0,1) eq ">") {$tmpfile .= ".fasta";}
        open SEQ,">/tmp/gb/$tmpfile";print SEQ $in0;close SEQ;$in0 = "/tmp/gb/".$tmpfile;
    }

    $in0 = new G::IO($in0,"no msg");
    my $scaler = "";
    require G::Seq::Codon;
    if ($param{-output} ne "f") {
        delete $param{-output};
        $scaler = G::Seq::Codon::codon_mva($in0,%param,-output=>"g",-filename=>"$jobid.png");
    } else {
        delete $param{-output};
        $scaler = G::Seq::Codon::codon_mva($in0,%param,-output=>"f",-filename=>"$jobid.csv");
    }

    $scaler = "http://soap.g-language.org/WS/result.cgi?jobid=$jobid";
    return SOAP::Data->type('string')->value($scaler);
}

sub P2{
    my $self = shift;
    my $in0 = shift;

    my %param = %{+shift};

    for ( keys %param ) {
        if ($param{$_} eq "") {delete $param{$_};}
        else {$param{"-$_"} = $param{$_};}
    }

    _set_sdb_path("/tmp/gb");

    G::Messenger::msg_interface("Inspire");
    my ($trpData,$trpError);
    G::Messenger::msg_term_console(sub{$trpData .= shift @_ });
    G::Messenger::msg_system_console(sub{$trpError .= shift @_ });

    my $jobid = time.substr(rand(10),-4);
    while (-e "./graph/".$jobid.".png" || -e "./data/".$jobid.".csv") {
        $jobid = time.substr(rand(10),-4);
    }

    if ( length($in0) > 10 ) {
        my $tmpfile = ( (time % 1296000)*10 + int(rand(10)) + 1048576);
        if (substr($in0,0,1) eq ">") {$tmpfile .= ".fasta";}
        open SEQ,">/tmp/gb/$tmpfile";print SEQ $in0;close SEQ;$in0 = "/tmp/gb/".$tmpfile;
    }

    $in0 = new G::IO($in0,"no msg");
    require G::Seq::Codon;
    my $scaler = G::Seq::Codon::P2($in0,%param,-output=>"f",-filename=>"$jobid.csv");

    $scaler = "http://soap.g-language.org/WS/result.cgi?jobid=$jobid";
    return SOAP::Data->type('string')->value($scaler);
}

sub w_value{
    my $self = shift;
    my $in0 = shift;

    my %param = %{+shift};

    for ( keys %param ) {
        if ($param{$_} eq "") {delete $param{$_};}
        else {$param{"-$_"} = $param{$_};}
    }

    _set_sdb_path("/tmp/gb");

    G::Messenger::msg_interface("Inspire");
    my ($trpData,$trpError);
    G::Messenger::msg_term_console(sub{$trpData .= shift @_ });
    G::Messenger::msg_system_console(sub{$trpError .= shift @_ });

    my $jobid = time.substr(rand(10),-4);
    while (-e "./graph/".$jobid.".png" || -e "./data/".$jobid.".csv") {
        $jobid = time.substr(rand(10),-4);
    }

    if ( length($in0) > 10 ) {
        my $tmpfile = ( (time % 1296000)*10 + int(rand(10)) + 1048576);
        if (substr($in0,0,1) eq ">") {$tmpfile .= ".fasta";}
        open SEQ,">/tmp/gb/$tmpfile";print SEQ $in0;close SEQ;$in0 = "/tmp/gb/".$tmpfile;
    }

    $in0 = new G::IO($in0,"no msg");
    require G::Seq::Codon;
    my $scaler = G::Seq::Codon::w_value($in0,%param,-output=>"f",-filename=>"$jobid.csv");

    $scaler = "http://soap.g-language.org/WS/result.cgi?jobid=$jobid";
    return SOAP::Data->type('string')->value($scaler);
}

sub splitprintseq{
    my $self = shift;
    my $in0 = shift;

    my %param = %{+shift};

    for ( keys %param ) {
        if ($param{$_} eq "") {delete $param{$_};}
        else {$param{"-$_"} = $param{$_};}
    }

    _set_sdb_path("/tmp/gb");

    G::Messenger::msg_interface("Inspire");
    my ($trpData,$trpError);
    G::Messenger::msg_term_console(sub{$trpData .= shift @_ });
    G::Messenger::msg_system_console(sub{$trpError .= shift @_ });

    my $jobid = time.substr(rand(10),-4);
    while (-e "./graph/".$jobid.".png" || -e "./data/".$jobid.".csv") {
        $jobid = time.substr(rand(10),-4);
    }


    require G::Seq::Primitive;    my $scaler = G::Seq::Primitive::splitprintseq($in0,%param);

    return SOAP::Data->type('string')->value($scaler);
}

sub median{
    my $self = shift;
    my @in0 = @{+shift};

    my %param = %{+shift};

    for ( keys %param ) {
        if ($param{$_} eq "") {delete $param{$_};}
        else {$param{"-$_"} = $param{$_};}
    }

    _set_sdb_path("/tmp/gb");

    G::Messenger::msg_interface("Inspire");
    my ($trpData,$trpError);
    G::Messenger::msg_term_console(sub{$trpData .= shift @_ });
    G::Messenger::msg_system_console(sub{$trpError .= shift @_ });

    my $jobid = time.substr(rand(10),-4);
    while (-e "./graph/".$jobid.".png" || -e "./data/".$jobid.".csv") {
        $jobid = time.substr(rand(10),-4);
    }


    require G::Tools::Statistics;    my $scaler = G::Tools::Statistics::median(@in0,%param);

    return SOAP::Data->type('string')->value($scaler);
}

sub find_ori_ter{
    my $self = shift;
    my $in0  = shift;

    my %param = %{+shift};

    for ( keys %param ) {
        if ($param{$_} eq "") {delete $param{$_};}
        else {$param{"-$_"} = $param{$_};}
    }

    if ( $param{"-filter"} !~ /^\d+$/ ) {
	$param{"-filter"} = "";
    }

    _set_sdb_path("/tmp/gb");

    G::Messenger::msg_interface("Inspire");
    my ($trpData,$trpError);
    G::Messenger::msg_term_console(sub{$trpData .= shift @_ });
    G::Messenger::msg_system_console(sub{$trpError .= shift @_ });

    my $jobid = time.substr(rand(10),-4);
    while (-e "./graph/".$jobid.".png" || -e "./data/".$jobid.".csv") {
        $jobid = time.substr(rand(10),-4);
    }

    if ( length($in0) > 10 ) {
        my $tmpfile = ( (time % 1296000)*10 + int(rand(10)) + 1048576);
        if (substr($in0,0,1) eq ">") {$tmpfile .= ".fasta";}
        open SEQ,">/tmp/gb/$tmpfile";print SEQ $in0;close SEQ;$in0 = "/tmp/gb/".$tmpfile;
    }

    $in0 = new G::IO($in0,"no msg");
    require G::Seq::GCskew;    my @array = G::Seq::GCskew::find_ori_ter($in0,%param);

    return SOAP::Data->type(array=>\@array);
}

sub plasmid_map{
    my $self = shift;
    my $in0 = shift;

    my %param = %{+shift};

    for ( keys %param ) {
        if ($param{$_} eq "") {delete $param{$_};}
        else {$param{"-$_"} = $param{$_};}
    }

    _set_sdb_path("/tmp/gb");

    G::Messenger::msg_interface("Inspire");
    my ($trpData,$trpError);
    G::Messenger::msg_term_console(sub{$trpData .= shift @_ });
    G::Messenger::msg_system_console(sub{$trpError .= shift @_ });

    my $jobid = time.substr(rand(10),-4);
    while (-e "./graph/".$jobid.".png" || -e "./data/".$jobid.".csv") {
        $jobid = time.substr(rand(10),-4);
    }

    if ($in0 ne "ecoli" && $in0 ne "bsub" && $in0 ne "mgen" && $in0 ne "cyano" && $in0 ne "pyro") {
        my $tmpfile = ( (time % 1296000)*10 + int(rand(10)) + 1048576);
        if (substr($in0,0,1) eq ">") {$tmpfile .= ".fasta";}
        open SEQ,">/tmp/gb/$tmpfile";print SEQ $in0;close SEQ;$in0 = "/tmp/gb/".$tmpfile;
    }

    $in0 = new G::IO($in0,"no msg");
    my $scaler = "";
    require G::Seq::GenomeMap;
    if ($param{-output} ne "f") {
        delete $param{-output};
        $scaler = G::Seq::GenomeMap::plasmid_map($in0,%param,-output=>"g",-filename=>"$jobid.png");
    } else {
        delete $param{-output};
        $scaler = G::Seq::GenomeMap::plasmid_map($in0,%param,-output=>"f",-filename=>"$jobid.csv");
    }

    $scaler = "http://soap.g-language.org/WS/result.cgi?jobid=$jobid";
    return SOAP::Data->type('string')->value($scaler);
}

sub sum {
    my $self = shift;
    my @in0 = @{+shift};

    my %param = %{+shift};

    for ( keys %param ) {
        if ($param{$_} eq "") {delete $param{$_};}
        else {$param{"-$_"} = $param{$_};}
    }

    _set_sdb_path("/tmp/gb");

    G::Messenger::msg_interface("Inspire");
    my ($trpData,$trpError);
    G::Messenger::msg_term_console(sub{$trpData .= shift @_ });
    G::Messenger::msg_system_console(sub{$trpError .= shift @_ });

    my $jobid = time.substr(rand(10),-4);
    while (-e "./graph/".$jobid.".png" || -e "./data/".$jobid.".csv") {
        $jobid = time.substr(rand(10),-4);
    }

    require G::Tools::Statistics;
    my $scaler = G::Tools::Statistics::sum(@in0,%param);

    return SOAP::Data->type('string')->value($scaler);
}

sub nucleotide_periodicity {
    my $self = shift;
    my $in0 = shift;

    my %param = %{+shift};

    for ( keys %param ) {
        if ($param{$_} eq "") {delete $param{$_};}
        else {$param{"-$_"} = $param{$_};}
    }

    _set_sdb_path("/tmp/gb");

    G::Messenger::msg_interface("Inspire");
    my ($trpData,$trpError);
    G::Messenger::msg_term_console(sub{$trpData .= shift @_ });
    G::Messenger::msg_system_console(sub{$trpError .= shift @_ });

    my $jobid = time.substr(rand(10),-4);
    while (-e "./graph/".$jobid.".png" || -e "./data/".$jobid.".csv") {
        $jobid = time.substr(rand(10),-4);
    }

    require G::Seq::PatSearch;

    delete $param{-output};
    G::Seq::PatSearch::nucleotide_periodicity($in0, %param, -output => "g", -filename => "$jobid.png");

    my $scaler = "http://soap.g-language.org/WS/result.cgi?jobid=$jobid";
    return SOAP::Data->type('string')->value($scaler);
}

sub variance{
    my $self = shift;
    my @in0 = @{+shift};

    my %param = %{+shift};

    for ( keys %param ) {
        if ($param{$_} eq "") {delete $param{$_};}
        else {$param{"-$_"} = $param{$_};}
    }

    _set_sdb_path("/tmp/gb");

    G::Messenger::msg_interface("Inspire");
    my ($trpData,$trpError);
    G::Messenger::msg_term_console(sub{$trpData .= shift @_ });
    G::Messenger::msg_system_console(sub{$trpError .= shift @_ });

    my $jobid = time.substr(rand(10),-4);
    while (-e "./graph/".$jobid.".png" || -e "./data/".$jobid.".csv") {
        $jobid = time.substr(rand(10),-4);
    }


    require G::Tools::Statistics;    my $scaler = G::Tools::Statistics::variance(@in0,%param);

    return SOAP::Data->type('string')->value($scaler);
}

sub amino_info{
    my $self = shift;
    my $in0 = shift;

    _set_sdb_path("/tmp/gb");

    G::Messenger::msg_interface("Inspire");
    my ($trpData,$trpError);
    G::Messenger::msg_term_console(sub{$trpData .= shift @_ });
    G::Messenger::msg_system_console(sub{$trpError .= shift @_ });

    require G::Seq::AminoAcid;;
    G::Seq::AminoAcid::amino_info($in0);

    return $trpData;
}

sub circular_map{
    my $self = shift;
    my $in0 = shift;

    my %param = %{+shift};

    for ( keys %param ) {
        if ($param{$_} eq "") {delete $param{$_};}
        else {$param{"-$_"} = $param{$_};}
    }

    _set_sdb_path("/tmp/gb");

    G::Messenger::msg_interface("Inspire");
    my ($trpData,$trpError);
    G::Messenger::msg_term_console(sub{$trpData .= shift @_ });
    G::Messenger::msg_system_console(sub{$trpError .= shift @_ });

    my $jobid = time.substr(rand(10),-4);
    while (-e "./graph/".$jobid.".png" || -e "./data/".$jobid.".csv") {
        $jobid = time.substr(rand(10),-4);
    }

    if ( length $in0 > 10 ) {
        my $tmpfile = ( (time % 1296000)*10 + int(rand(10)) + 1048576);
        if (substr($in0,0,1) eq ">") {$tmpfile .= ".fasta";}
        open SEQ,">/tmp/gb/$tmpfile";print SEQ $in0;close SEQ;$in0 = "/tmp/gb/".$tmpfile;
    }

    $in0 = new G::IO($in0,"no msg");
    my $scaler = "";
    require G::Seq::GenomeMap;
    if ($param{-output} ne "f") {
        delete $param{-output};
        $scaler = G::Seq::GenomeMap::circular_map($in0,%param,-output=>"g",-filename=>"$jobid.png");
    } else {
        delete $param{-output};
        $scaler = G::Seq::GenomeMap::circular_map($in0,%param,-output=>"f",-filename=>"$jobid.csv");
    }

    $scaler = "http://soap.g-language.org/WS/result.cgi?jobid=$jobid";
    return SOAP::Data->type('string')->value($scaler);
}

sub togoWS{
    my $self = shift;
    my $in0 = shift;

    my %param;
    if (ref $_[0] eq 'togoWSInputParams') {
        %param = %{+shift};
    } else {
        %param = @_;
    }

    for ( keys %param ) {
        if ($param{$_} eq "") {delete $param{$_};}
        else {$param{"-$_"} = $param{$_};}
    }
    _set_sdb_path("/tmp/gb");

    G::Messenger::msg_interface("Inspire");
    my ($trpData,$trpError);
    G::Messenger::msg_term_console(sub{$trpData .= shift @_ });
    G::Messenger::msg_system_console(sub{$trpError .= shift @_ });

    require G::Tools::WebServices;

    my $scaler = '';
    if ( $in0 =~ m{ [,] }x ) {
	$in0 =~ s/\s//;
	my @in0 = split(/,/, $in0);
	$scaler = G::Tools::WebServices::togoWS(@in0,%param);
    } else {
	$scaler = G::Tools::WebServices::togoWS($in0,%param);
    }

    return SOAP::Data->type('string')->value($scaler);
}

sub translate{
    my $self = shift;
    my $in0 = shift;

    my %param = %{+shift};

    for ( keys %param ) {
        if ($param{$_} eq "") {delete $param{$_};}
        else {$param{"-$_"} = $param{$_};}
    }

    _set_sdb_path("/tmp/gb");

    G::Messenger::msg_interface("Inspire");
    my ($trpData,$trpError);
    G::Messenger::msg_term_console(sub{$trpData .= shift @_ });
    G::Messenger::msg_system_console(sub{$trpError .= shift @_ });

    my $jobid = time.substr(rand(10),-4);
    while (-e "./graph/".$jobid.".png" || -e "./data/".$jobid.".csv") {
        $jobid = time.substr(rand(10),-4);
    }


    require G;    my $scaler = G::translate($in0,%param);

    return SOAP::Data->type('string')->value($scaler);
}

sub phx{
    my $self = shift;
    my $in0 = shift;

    my %param = %{+shift};

    for ( keys %param ) {
        if ($param{$_} eq "") {delete $param{$_};}
        else {$param{"-$_"} = $param{$_};}
    }

    delete $param{"-usage"} unless $param{"-usage"};


    _set_sdb_path("/tmp/gb");

    G::Messenger::msg_interface("Inspire");
    my ($trpData,$trpError);
    G::Messenger::msg_term_console(sub{$trpData .= shift @_ });
    G::Messenger::msg_system_console(sub{$trpError .= shift @_ });

    my $jobid = time.substr(rand(10),-4);
    while (-e "./graph/".$jobid.".png" || -e "./data/".$jobid.".csv") {
        $jobid = time.substr(rand(10),-4);
    }

    if ( length($in0) > 10 ) {
        my $tmpfile = ( (time % 1296000)*10 + int(rand(10)) + 1048576);
        if (substr($in0,0,1) eq ">") {$tmpfile .= ".fasta";}
        open SEQ,">/tmp/gb/$tmpfile";print SEQ $in0;close SEQ;$in0 = "/tmp/gb/".$tmpfile;
    }

    $in0 = new G::IO($in0,"no msg");

    require G::Seq::Codon;
    my $scaler = G::Seq::Codon::phx($in0,%param,-output=>"f",-filename=>"$jobid.csv");

    $scaler = "http://soap.g-language.org/WS/result.cgi?jobid=$jobid";
    return SOAP::Data->type('string')->value($scaler);
}

sub icdi{
    my $self = shift;
    my $in0 = shift;

    my %param = %{+shift};

    for ( keys %param ) {
        if ($param{$_} eq "") {delete $param{$_};}
        else {$param{"-$_"} = $param{$_};}
    }

    if ( lc($param{"-id"}) eq 'all' ) {
        $param{"-id"} = "All";
    }

    _set_sdb_path("/tmp/gb");

    G::Messenger::msg_interface("Inspire");
    my ($trpData,$trpError);
    G::Messenger::msg_term_console(sub{$trpData .= shift @_ });
    G::Messenger::msg_system_console(sub{$trpError .= shift @_ });

    my $jobid = time.substr(rand(10),-4);
    while (-e "./graph/".$jobid.".png" || -e "./data/".$jobid.".csv") {
        $jobid = time.substr(rand(10),-4);
    }

    if ( length($in0) > 10 ) {
        my $tmpfile = ( (time % 1296000)*10 + int(rand(10)) + 1048576);
        if (substr($in0,0,1) eq ">") {$tmpfile .= ".fasta";}
        open SEQ,">/tmp/gb/$tmpfile";print SEQ $in0;close SEQ;$in0 = "/tmp/gb/".$tmpfile;
    }

    $in0 = new G::IO($in0,"no msg");
    require G::Seq::Codon;    my $scaler = G::Seq::Codon::icdi($in0,%param);

    return SOAP::Data->type('string')->value($scaler);
}

sub enc{
    my $self = shift;
    my $in0 = shift;

    my %param = %{+shift};

    for ( keys %param ) {
        if ($param{$_} eq "") {delete $param{$_};}
        else {$param{"-$_"} = $param{$_};}
    }

    _set_sdb_path("/tmp/gb");

    G::Messenger::msg_interface("Inspire");
    my ($trpData,$trpError);
    G::Messenger::msg_term_console(sub{$trpData .= shift @_ });
    G::Messenger::msg_system_console(sub{$trpError .= shift @_ });

    my $jobid = time.substr(rand(10),-4);
    while (-e "./graph/".$jobid.".png" || -e "./data/".$jobid.".csv") {
        $jobid = time.substr(rand(10),-4);
    }

    if ( length $in0 > 10 ) {
        my $tmpfile = ( (time % 1296000)*10 + int(rand(10)) + 1048576);
        if (substr($in0,0,1) eq ">") {$tmpfile .= ".fasta";}
        open SEQ,">/tmp/gb/$tmpfile";print SEQ $in0;close SEQ;$in0 = "/tmp/gb/".$tmpfile;
    }

    $in0 = new G::IO($in0,"no msg");
    require G::Seq::Codon;    my $scaler = G::Seq::Codon::enc($in0,%param);

    return SOAP::Data->type('string')->value($scaler);
}

sub fop{
    my $self = shift;
    my $in0 = shift;

    my %param = %{+shift};

    for ( keys %param ) {
        if ($param{$_} eq "") {delete $param{$_};}
        else {$param{"-$_"} = $param{$_};}
    }

    _set_sdb_path("/tmp/gb");

    G::Messenger::msg_interface("Inspire");
    my ($trpData,$trpError);
    G::Messenger::msg_term_console(sub{$trpData .= shift @_ });
    G::Messenger::msg_system_console(sub{$trpError .= shift @_ });

    my $jobid = time.substr(rand(10),-4);
    while (-e "./graph/".$jobid.".png" || -e "./data/".$jobid.".csv") {
        $jobid = time.substr(rand(10),-4);
    }

    if ( length($in0) > 10 ) {
        my $tmpfile = ( (time % 1296000)*10 + int(rand(10)) + 1048576);
        if (substr($in0,0,1) eq ">") {$tmpfile .= ".fasta";}
        open SEQ,">/tmp/gb/$tmpfile";print SEQ $in0;close SEQ;$in0 = "/tmp/gb/".$tmpfile;
    }

    $in0 = new G::IO($in0,"no msg");
    require G::Seq::Codon;
    my $scaler = G::Seq::Codon::fop($in0,%param,-output=>"f",-filename=>"$jobid.csv");

    $scaler = "http://soap.g-language.org/WS/result.cgi?jobid=$jobid";
    return SOAP::Data->type('string')->value($scaler);
}

sub bui{
    my $self = shift;
    my $in0  = shift;

    my %param = %{+shift};

    for ( keys %param ) {
        if ($param{$_} eq "") {delete $param{$_};}
        else {$param{"-$_"} = $param{$_};}
    }

    if ( lc($param{"-id"}) eq 'all' ) {
        $param{"-id"} = "All";
    }

    _set_sdb_path("/tmp/gb");

    G::Messenger::msg_interface("Inspire");
    my ($trpData,$trpError);
    G::Messenger::msg_term_console(sub{$trpData .= shift @_ });
    G::Messenger::msg_system_console(sub{$trpError .= shift @_ });

    my $jobid = time.substr(rand(10),-4);
    while (-e "./graph/".$jobid.".png" || -e "./data/".$jobid.".csv") {
        $jobid = time.substr(rand(10),-4);
    }

    if ( length($in0) > 10 ) {
        my $tmpfile = ( (time % 1296000)*10 + int(rand(10)) + 1048576);
        if (substr($in0,0,1) eq ">") {$tmpfile .= ".fasta";}
        open SEQ,">/tmp/gb/$tmpfile";print SEQ $in0;close SEQ;$in0 = "/tmp/gb/".$tmpfile;
    }

    $in0 = new G::IO($in0,"no msg");
    require G::Seq::Codon;
    my $scaler = G::Seq::Codon::bui($in0,%param,-output=>"f",-filename=>"$jobid.csv");

    unless ( -e "./data/$jobid.csv" ) {
	`touch ./data/$jobid.csv`;
    }

    $scaler = "http://soap.g-language.org/WS/result.cgi?jobid=$jobid";
    return SOAP::Data->type('string')->value($scaler);
}

sub dist_in_cc{
    my $self = shift;
    my $in0 = shift;
    my $in1 = shift;
    my $in2 = shift;

    my %param = %{+shift};

    for ( keys %param ) {
        if ($param{$_} eq "") {delete $param{$_};}
        else {$param{"-$_"} = $param{$_};}
    }

    _set_sdb_path("/tmp/gb");

    G::Messenger::msg_interface("Inspire");
    my ($trpData,$trpError);
    G::Messenger::msg_term_console(sub{$trpData .= shift @_ });
    G::Messenger::msg_system_console(sub{$trpError .= shift @_ });

    my $jobid = time.substr(rand(10),-4);
    while (-e "./graph/".$jobid.".png" || -e "./data/".$jobid.".csv") {
        $jobid = time.substr(rand(10),-4);
    }

    if ( length $in0 > 10 ) {
        my $tmpfile = ( (time % 1296000)*10 + int(rand(10)) + 1048576);
        if (substr($in0,0,1) eq ">") {$tmpfile .= ".fasta";}
        open SEQ,">/tmp/gb/$tmpfile";print SEQ $in0;close SEQ;$in0 = "/tmp/gb/".$tmpfile;
    }

    $in0 = new G::IO($in0,"no msg");
    require G::Seq::GCskew;    my $scaler = G::Seq::GCskew::dist_in_cc($in0,$in1,$in2,%param);

    return SOAP::Data->type('string')->value($scaler);
}

sub find_dnaAbox{
    my $self = shift;
    my $in0 = shift;

    my %param = %{+shift};

    for ( keys %param ) {
        if ($param{$_} eq "") {delete $param{$_};}
        else {$param{"-$_"} = $param{$_};}
    }

    _set_sdb_path("/tmp/gb");

    G::Messenger::msg_interface("Inspire");
    my ($trpData,$trpError);
    G::Messenger::msg_term_console(sub{$trpData .= shift @_ });
    G::Messenger::msg_system_console(sub{$trpError .= shift @_ });

    my $jobid = time.substr(rand(10),-4);
    while (-e "./graph/".$jobid.".png" || -e "./data/".$jobid.".csv") {
        $jobid = time.substr(rand(10),-4);
    }

    if ($in0 ne "ecoli" && $in0 ne "bsub" && $in0 ne "mgen" && $in0 ne "cyano" && $in0 ne "pyro") {
        my $tmpfile = ( (time % 1296000)*10 + int(rand(10)) + 1048576);
        if (substr($in0,0,1) eq ">") {$tmpfile .= ".fasta";}
        open SEQ,">/tmp/gb/$tmpfile";print SEQ $in0;close SEQ;$in0 = "/tmp/gb/".$tmpfile;
    }

    $in0 = new G::IO($in0,"no msg");
    require G::Seq::PatSearch;    my @array = G::Seq::PatSearch::find_dnaAbox($in0,%param);

    return SOAP::Data->type(array=>\@array);
}

sub ttest{
    my $self = shift;
    my @in0 = @{+shift};
    my @in1 = @{+shift};

    my %param = %{+shift};

    for ( keys %param ) {
        if ($param{$_} eq "") {delete $param{$_};}
        else {$param{"-$_"} = $param{$_};}
    }

    _set_sdb_path("/tmp/gb");

    G::Messenger::msg_interface("Inspire");
    my ($trpData,$trpError);
    G::Messenger::msg_term_console(sub{$trpData .= shift @_ });
    G::Messenger::msg_system_console(sub{$trpError .= shift @_ });

    my $jobid = time.substr(rand(10),-4);
    while (-e "./graph/".$jobid.".png" || -e "./data/".$jobid.".csv") {
        $jobid = time.substr(rand(10),-4);
    }


    require G::Tools::Statistics;    my @array = G::Tools::Statistics::ttest(\@in0,\@in1,%param);

    return SOAP::Data->type(array=>\@array);
}

sub seq2png{
    my $self = shift;
    my $in0 = shift;

    my %param = %{+shift};

    for ( keys %param ) {
        if ($param{$_} eq "") {delete $param{$_};}
        else {$param{"-$_"} = $param{$_};}
    }

    _set_sdb_path("/tmp/gb");

    G::Messenger::msg_interface("Inspire");
    my ($trpData,$trpError);
    G::Messenger::msg_term_console(sub{$trpData .= shift @_ });
    G::Messenger::msg_system_console(sub{$trpError .= shift @_ });

    my $jobid = time.substr(rand(10),-4);
    while (-e "./graph/".$jobid.".png" || -e "./data/".$jobid.".csv") {
        $jobid = time.substr(rand(10),-4);
    }

    if ($in0 ne "ecoli" && $in0 ne "bsub" && $in0 ne "mgen" && $in0 ne "cyano" && $in0 ne "pyro") {
        my $tmpfile = ( (time % 1296000)*10 + int(rand(10)) + 1048576);
        if (substr($in0,0,1) eq ">") {$tmpfile .= ".fasta";}
        open SEQ,">/tmp/gb/$tmpfile";print SEQ $in0;close SEQ;$in0 = "/tmp/gb/".$tmpfile;
    }

    $in0 = new G::IO($in0,"no msg");
    require G::Seq::GenomeMap;
    my $scaler = G::Seq::GenomeMap::seq2png($in0,%param,-output=>"g",-filename=>"$jobid.png");

    $scaler = "http://soap.g-language.org/WS/result.cgi?jobid=$jobid";
    return SOAP::Data->type('string')->value($scaler);
}

sub amino_counter{
    my $self = shift;
    my $in0 = shift;

    my %param = %{+shift};

    for ( keys %param ) {
        if ($param{$_} eq "") {delete $param{$_};}
        else {$param{"-$_"} = $param{$_};}
    }

    _set_sdb_path("/tmp/gb");

    G::Messenger::msg_interface("Inspire");
    my ($trpData,$trpError);
    G::Messenger::msg_term_console(sub{$trpData .= shift @_ });
    G::Messenger::msg_system_console(sub{$trpError .= shift @_ });

    my $jobid = time.substr(rand(10),-4);
    while (-e "./graph/".$jobid.".png" || -e "./data/".$jobid.".csv") {
        $jobid = time.substr(rand(10),-4);
    }

    if ($in0 ne "ecoli" && $in0 ne "bsub" && $in0 ne "mgen" && $in0 ne "cyano" && $in0 ne "pyro") {
        my $tmpfile = ( (time % 1296000)*10 + int(rand(10)) + 1048576);
        if (substr($in0,0,1) eq ">") {$tmpfile .= ".fasta";}
        open SEQ,">/tmp/gb/$tmpfile";print SEQ $in0;close SEQ;$in0 = "/tmp/gb/".$tmpfile;
    }

    $in0 = new G::IO($in0,"no msg");
    my @array = "";
    require G::Seq::Codon;
    if ($param{-output} ne "f") {
        delete $param{-output};
        @array = G::Seq::Codon::amino_counter($in0,%param,-output=>"g",-filename=>"$jobid.png");
    } else {
        delete $param{-output};
        @array = G::Seq::Codon::amino_counter($in0,%param,-output=>"f",-filename=>"$jobid.csv");
    }

    $scaler = "http://soap.g-language.org/WS/result.cgi?jobid=$jobid";
    return SOAP::Data->type('string')->value($scaler);
}

sub aaui {
    my $self = shift;
    my $in0  = shift;

    my %param = %{+shift};

    for ( keys %param ) {
        if ($param{$_} eq "") {delete $param{$_};}
        else {$param{"-$_"} = $param{$_};}
    }

    _set_sdb_path("/tmp/gb");

    G::Messenger::msg_interface("Inspire");
    my ($trpData,$trpError);
    G::Messenger::msg_term_console(sub{$trpData .= shift @_ });
    G::Messenger::msg_system_console(sub{$trpError .= shift @_ });

    my $jobid = time.substr(rand(10),-4);
    while (-e "./graph/".$jobid.".png" || -e "./data/".$jobid.".csv") {
        $jobid = time.substr(rand(10),-4);
    }

    if ( length $in0 > 10 ) {
        my $tmpfile = ( (time % 1296000)*10 + int(rand(10)) + 1048576);
        if (substr($in0,0,1) eq ">") {$tmpfile .= ".fasta";}
        open SEQ,">/tmp/gb/$tmpfile";print SEQ $in0;close SEQ;$in0 = "/tmp/gb/".$tmpfile;
    }

    $in0 = new G::IO($in0,"no msg");
    require G::Seq::Codon;
    G::Seq::Codon::aaui($in0,%param,-output=>"f",-filename=>"$jobid.csv");

    unless ( -e "./data/$jobid.csv" ) {
	`touch ./data/$jobid.csv`;
    }

    my $scaler = "http://soap.g-language.org/WS/result.cgi?jobid=$jobid";
    return SOAP::Data->type('string')->value($scaler);
}

sub codon_compiler{
    my $self = shift;
    my $in0 = shift;

    my %param = %{+shift};

    for ( keys %param ) {
        if ($param{$_} eq "") {delete $param{$_};}
        else {$param{"-$_"} = $param{$_};}
    }

    _set_sdb_path("/tmp/gb");

    G::Messenger::msg_interface("Inspire");
    my ($trpData,$trpError);
    G::Messenger::msg_term_console(sub{$trpData .= shift @_ });
    G::Messenger::msg_system_console(sub{$trpError .= shift @_ });

    my $jobid = time.substr(rand(10),-4);
    while (-e "./graph/".$jobid.".png" || -e "./data/".$jobid.".csv") {
        $jobid = time.substr(rand(10),-4);
    }

    if ( length $in0 > 10 ) {
        my $tmpfile = ( (time % 1296000)*10 + int(rand(10)) + 1048576);
        if (substr($in0,0,1) eq ">") {$tmpfile .= ".fasta";}
        open SEQ,">/tmp/gb/$tmpfile";print SEQ $in0;close SEQ;$in0 = "/tmp/gb/".$tmpfile;
    }

    $in0 = new G::IO($in0,"no msg");
    my $scaler = "";
    require G::Seq::Codon;
    if ($param{-output} ne "f") {
        delete $param{-output};
        $scaler = G::Seq::Codon::codon_compiler($in0,%param,-output=>"g",-filename=>"$jobid.png");
    } else {
        delete $param{-output};
        $scaler = G::Seq::Codon::codon_compiler($in0,%param,-output=>"f",-filename=>"$jobid.csv");
    }

    $scaler = "http://soap.g-language.org/WS/result.cgi?jobid=$jobid";
    return SOAP::Data->type('string')->value($scaler);
}

sub over_lapping_finder{
    my $self = shift;
    my $in0 = shift;

    my %param = %{+shift};

    for ( keys %param ) {
        if ($param{$_} eq "") {delete $param{$_};}
        else {$param{"-$_"} = $param{$_};}
    }

    _set_sdb_path("/tmp/gb");

    G::Messenger::msg_interface("Inspire");
    my ($trpData,$trpError);
    G::Messenger::msg_term_console(sub{$trpData .= shift @_ });
    G::Messenger::msg_system_console(sub{$trpError .= shift @_ });

    my $jobid = time.substr(rand(10),-4);
    while (-e "./graph/".$jobid.".png" || -e "./data/".$jobid.".csv") {
        $jobid = time.substr(rand(10),-4);
    }

    if ($in0 ne "ecoli" && $in0 ne "bsub" && $in0 ne "mgen" && $in0 ne "cyano" && $in0 ne "pyro") {
        my $tmpfile = ( (time % 1296000)*10 + int(rand(10)) + 1048576);
        if (substr($in0,0,1) eq ">") {$tmpfile .= ".fasta";}
        open SEQ,">/tmp/gb/$tmpfile";print SEQ $in0;close SEQ;$in0 = "/tmp/gb/".$tmpfile;
    }

    $in0 = new G::IO($in0,"no msg");
    require G::Seq::OverLapping;    my $scaler = G::Seq::OverLapping::over_lapping_finder($in0,%param);

    return SOAP::Data->type('string')->value($scaler);
}

sub Ew{
    my $self = shift;
    my $in0 = shift;

    my %param = %{+shift};

    for ( keys %param ) {
        if ($param{$_} eq "") {delete $param{$_};}
        else {$param{"-$_"} = $param{$_};}
    }

    _set_sdb_path("/tmp/gb");

    G::Messenger::msg_interface("Inspire");
    my ($trpData,$trpError);
    G::Messenger::msg_term_console(sub{$trpData .= shift @_ });
    G::Messenger::msg_system_console(sub{$trpError .= shift @_ });

    my $jobid = time.substr(rand(10),-4);
    while (-e "./graph/".$jobid.".png" || -e "./data/".$jobid.".csv") {
        $jobid = time.substr(rand(10),-4);
    }

    if ( length $in0 > 10 ) {
        my $tmpfile = ( (time % 1296000)*10 + int(rand(10)) + 1048576);
        if (substr($in0,0,1) eq ">") {$tmpfile .= ".fasta";}
        open SEQ,">/tmp/gb/$tmpfile";print SEQ $in0;close SEQ;$in0 = "/tmp/gb/".$tmpfile;
    }

    $in0 = new G::IO($in0,"no msg");
    require G::Seq::Codon;
    my $scaler = G::Seq::Codon::Ew($in0,%param,-output=>"f",-filename=>"$jobid.csv");

    $scaler = "http://soap.g-language.org/WS/result.cgi?jobid=$jobid";
    return SOAP::Data->type('string')->value($scaler);
}

sub base_relative_entropy{
    my $self = shift;
    my $in0 = shift;

    my %param = %{+shift};

    for ( keys %param ) {
        if ($param{$_} eq "") {delete $param{$_};}
        else {$param{"-$_"} = $param{$_};}
    }

    _set_sdb_path("/tmp/gb");

    G::Messenger::msg_interface("Inspire");
    my ($trpData,$trpError);
    G::Messenger::msg_term_console(sub{$trpData .= shift @_ });
    G::Messenger::msg_system_console(sub{$trpError .= shift @_ });

    my $jobid = time.substr(rand(10),-4);
    while (-e "./graph/".$jobid.".png" || -e "./data/".$jobid.".csv") {
        $jobid = time.substr(rand(10),-4);
    }

    if ( length $in0 > 10 ) {
        my $tmpfile = ( (time % 1296000)*10 + int(rand(10)) + 1048576);
        if (substr($in0,0,1) eq ">") {$tmpfile .= ".fasta";}
        open SEQ,">/tmp/gb/$tmpfile";print SEQ $in0;close SEQ;$in0 = "/tmp/gb/".$tmpfile;
    }

    $in0 = new G::IO($in0,"no msg");
    my $scaler = "";
    require G::Seq::Consensus;
    if ($param{-output} ne "f") {
        delete $param{-output};
        $scaler = G::Seq::Consensus::base_relative_entropy($in0,%param,-output=>"g",-filename=>"$jobid.png");
    } else {
        delete $param{-output};
        $scaler = G::Seq::Consensus::base_relative_entropy($in0,%param,-output=>"f",-filename=>"$jobid.csv");
    }

    $scaler = "http://soap.g-language.org/WS/result.cgi?jobid=$jobid";
    return SOAP::Data->type('string')->value($scaler);
}

sub view_cds {
    my $self= shift;
    my $in0=  shift;

    my %param= %{+shift};
    for (keys %param) {
        if ($param{$_} eq '') {
	    delete $param{$_};
	} else {
	    $param{"-$_"}= $param{$_};
	}
    }

    _set_sdb_path('/tmp/gb');

    G::Messenger::msg_interface('Inspire');
    my ($trpData,$trpError);
    G::Messenger::msg_term_console(  sub{$trpData.=  shift @_ });
    G::Messenger::msg_system_console(sub{$trpError.= shift @_ });

    my $jobid= time.substr(rand(10), -4);
    while (-e './graph/'.$jobid.'.png' || -e './data/'.$jobid.'.csv') {
        $jobid= time.substr(rand(10), -4);
    }

    if (length($in0) > 10) {
        my $tmpfile= ((time % 1296000)*10 + int(rand(10)) + 1048576);
        if (substr($in0, 0, 1) eq '>') {
	    $tmpfile.= '.fasta';
	}
        open my $SEQ, '>', '/tmp/gb/'.$tmpfile;
	print $SEQ $in0;
	close $SEQ;

	$in0= '/tmp/gb/'.$tmpfile;
    }

    $in0= new G::IO($in0, 'no msg');

    require G::Seq::Util;
    if ($param{-output} ne 'f') {
        delete $param{-output};
	G::Seq::Util::view_cds($in0, %param, -output => 'g', -filename => "$jobid.png");
    } else {
        delete $param{-output};
	G::Seq::Util::view_cds($in0, %param, -output => 'f', -filename => "$jobid.csv");
    }

    my $scaler= "http://soap.g-language.org/WS/result.cgi?jobid=$jobid";
    return SOAP::Data->type('string')->value($scaler);
}

sub query_strand{
    my $self = shift;
    my $in0 = shift;
    my $in1 = shift;

    my %param = %{+shift};

    for ( keys %param ) {
        if ($param{$_} eq "") {delete $param{$_};}
        else {$param{"-$_"} = $param{$_};}
    }

    _set_sdb_path("/tmp/gb");

    G::Messenger::msg_interface("Inspire");
    my ($trpData,$trpError);
    G::Messenger::msg_term_console(sub{$trpData .= shift @_ });
    G::Messenger::msg_system_console(sub{$trpError .= shift @_ });

    my $jobid = time.substr(rand(10),-4);
    while (-e "./graph/".$jobid.".png" || -e "./data/".$jobid.".csv") {
        $jobid = time.substr(rand(10),-4);
    }

    if ( length($in0) > 10 ) {
        my $tmpfile = ( (time % 1296000)*10 + int(rand(10)) + 1048576);
        if (substr($in0,0,1) eq ">") {$tmpfile .= ".fasta";}
        open SEQ,">/tmp/gb/$tmpfile";print SEQ $in0;close SEQ;$in0 = "/tmp/gb/".$tmpfile;
    }

    $in0 = new G::IO($in0,"no msg");
    require G::Seq::GCskew;    my $scaler = G::Seq::GCskew::query_strand($in0,$in1,%param);

    return SOAP::Data->type('string')->value($scaler);
}

sub genomicskew {
    my $self = shift;
    my $in0  = shift;

    my %param = %{+shift};

    for ( keys %param ) {
        if ($param{$_} eq "") {delete $param{$_};}
        else {$param{"-$_"} = $param{$_};}
    }

    _set_sdb_path("/tmp/gb");

    G::Messenger::msg_interface("Inspire");
    my ($trpData,$trpError);
    G::Messenger::msg_term_console(sub{$trpData .= shift @_ });
    G::Messenger::msg_system_console(sub{$trpError .= shift @_ });

    my $jobid = time.substr(rand(10),-4);
    while (-e "./graph/".$jobid.".png" || -e "./data/".$jobid.".csv") {
        $jobid = time.substr(rand(10),-4);
    }

    if ( length($in0) > 10 ) {
        my $tmpfile = ( (time % 1296000)*10 + int(rand(10)) + 1048576);
        if (substr($in0,0,1) eq ">") {$tmpfile .= ".fasta";}
        open SEQ,">/tmp/gb/$tmpfile";print SEQ $in0;close SEQ;$in0 = "/tmp/gb/".$tmpfile;
    }

    $in0 = new G::IO($in0,"no msg");
    my $scaler = "";
    require G::Seq::GCskew;
    if ($param{-output} ne "f") {
        delete $param{-output};
        $scaler = G::Seq::GCskew::genomicskew($in0, %param, -output=>"g",-filename=>"$jobid.png");
    } else {
        delete $param{-output};
        $scaler = G::Seq::GCskew::genomicskew($in0, %param, -output=>"f",-filename=>"$jobid.csv");
    }

    $scaler = "http://soap.g-language.org/WS/result.cgi?jobid=$jobid";
    return SOAP::Data->type('string')->value($scaler);
}

sub filter_cds_by_atg{
    my $self = shift;
    my $in0 = shift;

    my %param = %{+shift};

    for ( keys %param ) {
        if ($param{$_} eq "") {delete $param{$_};}
        else {$param{"-$_"} = $param{$_};}
    }

    _set_sdb_path("/tmp/gb");

    G::Messenger::msg_interface("Inspire");
    my ($trpData,$trpError);
    G::Messenger::msg_term_console(sub{$trpData .= shift @_ });
    G::Messenger::msg_system_console(sub{$trpError .= shift @_ });

    my $jobid = time.substr(rand(10),-4);
    while (-e "./graph/".$jobid.".png" || -e "./data/".$jobid.".csv") {
        $jobid = time.substr(rand(10),-4);
    }

    if ($in0 ne "ecoli" && $in0 ne "bsub" && $in0 ne "mgen" && $in0 ne "cyano" && $in0 ne "pyro") {
        my $tmpfile = ( (time % 1296000)*10 + int(rand(10)) + 1048576);
        if (substr($in0,0,1) eq ">") {$tmpfile .= ".fasta";}
        open SEQ,">/tmp/gb/$tmpfile";print SEQ $in0;close SEQ;$in0 = "/tmp/gb/".$tmpfile;
    }

    $in0 = new G::IO($in0,"no msg");
    require G::Seq::Util;    my @array = G::Seq::Util::filter_cds_by_atg($in0,%param);

    return SOAP::Data->type(array=>\@array);
}

sub gcsi{
    my $self = shift;
    my $in0 = shift;

    my %param = %{+shift};

    for ( keys %param ) {
        if ($param{$_} eq "") {delete $param{$_};}
        else {$param{"-$_"} = $param{$_};}
    }

    _set_sdb_path("/tmp/gb");

    G::Messenger::msg_interface("Inspire");
    my ($trpData,$trpError);
    G::Messenger::msg_term_console(sub{$trpData .= shift @_ });
    G::Messenger::msg_system_console(sub{$trpError .= shift @_ });

    my $jobid = time.substr(rand(10),-4);
    while (-e "./graph/".$jobid.".png" || -e "./data/".$jobid.".csv") {
        $jobid = time.substr(rand(10),-4);
    }

    if ( length($in0) > 10 ) {
        my $tmpfile = ( (time % 1296000)*10 + int(rand(10)) + 1048576);
        if (substr($in0,0,1) eq ">") {$tmpfile .= ".fasta";}
        open SEQ,">/tmp/gb/$tmpfile";print SEQ $in0;close SEQ;$in0 = "/tmp/gb/".$tmpfile;
    }

    $in0 = new G::IO($in0,"no msg");
    require G::Seq::GCskew;    my @array = G::Seq::GCskew::gcsi($in0,%param);

    return SOAP::Data->type(array=>\@array);
}

sub cai{
    my $self = shift;
    my $in0 = shift;

    my %param = %{+shift};

    for ( keys %param ) {
        if ($param{$_} eq "") {delete $param{$_};}
        else {$param{"-$_"} = $param{$_};}
    }

    _set_sdb_path("/tmp/gb");

    G::Messenger::msg_interface("Inspire");
    my ($trpData,$trpError);
    G::Messenger::msg_term_console(sub{$trpData .= shift @_ });
    G::Messenger::msg_system_console(sub{$trpError .= shift @_ });

    my $jobid = time.substr(rand(10),-4);
    while (-e "./graph/".$jobid.".png" || -e "./data/".$jobid.".csv") {
        $jobid = time.substr(rand(10),-4);
    }

    if ( length($in0) > 10 ) {
        my $tmpfile = ( (time % 1296000)*10 + int(rand(10)) + 1048576);
        if (substr($in0,0,1) eq ">") {$tmpfile .= ".fasta";}
        open SEQ,">/tmp/gb/$tmpfile";print SEQ $in0;close SEQ;$in0 = "/tmp/gb/".$tmpfile;
    }

    $in0 = new G::IO($in0,"no msg");
    require G::Seq::Codon;
    my $scaler = G::Seq::Codon::cai($in0,%param,-output=>"f",-filename=>"$jobid.csv");

    $scaler = "http://soap.g-language.org/WS/result.cgi?jobid=$jobid";
    return SOAP::Data->type('string')->value($scaler);
}

sub maxdex{
    my $self = shift;
    my @in0 = @{+shift};

    my %param = %{+shift};

    for ( keys %param ) {
        if ($param{$_} eq "") {delete $param{$_};}
        else {$param{"-$_"} = $param{$_};}
    }

    _set_sdb_path("/tmp/gb");

    G::Messenger::msg_interface("Inspire");
    my ($trpData,$trpError);
    G::Messenger::msg_term_console(sub{$trpData .= shift @_ });
    G::Messenger::msg_system_console(sub{$trpError .= shift @_ });

    my $jobid = time.substr(rand(10),-4);
    while (-e "./graph/".$jobid.".png" || -e "./data/".$jobid.".csv") {
        $jobid = time.substr(rand(10),-4);
    }


    require G::Tools::Statistics;    my $scaler = G::Tools::Statistics::maxdex(@in0,%param);

    return SOAP::Data->type('string')->value($scaler);
}

sub max{
    my $self = shift;
    my @in0 = @{+shift};

    _set_sdb_path("/tmp/gb");

    G::Messenger::msg_interface("Inspire");
    my ($trpData,$trpError);
    G::Messenger::msg_term_console(sub{$trpData .= shift @_ });
    G::Messenger::msg_system_console(sub{$trpError .= shift @_ });

    my $jobid = time.substr(rand(10),-4);
    while (-e "./graph/".$jobid.".png" || -e "./data/".$jobid.".csv") {
        $jobid = time.substr(rand(10),-4);
    }

    require G::Tools::Statistics;    my $scaler = G::Tools::Statistics::max(@in0);

    return SOAP::Data->type('string')->value($scaler);
}

sub query_arm{
    my $self = shift;
    my $in0 = shift;
    my $in1 = shift;

    _set_sdb_path("/tmp/gb");

    G::Messenger::msg_interface("Inspire");
    my ($trpData,$trpError);
    G::Messenger::msg_term_console(sub{$trpData .= shift @_ });
    G::Messenger::msg_system_console(sub{$trpError .= shift @_ });

    my $jobid = time.substr(rand(10),-4);
    while (-e "./graph/".$jobid.".png" || -e "./data/".$jobid.".csv") {
        $jobid = time.substr(rand(10),-4);
    }

    if ( length($in0) > 10 ) {
        my $tmpfile = ( (time % 1296000)*10 + int(rand(10)) + 1048576);
        if (substr($in0,0,1) eq ">") {$tmpfile .= ".fasta";}
        open SEQ,">/tmp/gb/$tmpfile";print SEQ $in0;close SEQ;$in0 = "/tmp/gb/".$tmpfile;
    }

    $in0 = new G::IO($in0,"no msg");
    require G::Seq::GCskew;    my $scaler = G::Seq::GCskew::query_arm($in0,$in1);

    return SOAP::Data->type('string')->value($scaler);
}

sub mindex{
    my $self = shift;
    my @in0 = @{+shift};

    my %param = %{+shift};

    for ( keys %param ) {
        if ($param{$_} eq "") {delete $param{$_};}
        else {$param{"-$_"} = $param{$_};}
    }

    _set_sdb_path("/tmp/gb");

    G::Messenger::msg_interface("Inspire");
    my ($trpData,$trpError);
    G::Messenger::msg_term_console(sub{$trpData .= shift @_ });
    G::Messenger::msg_system_console(sub{$trpError .= shift @_ });

    my $jobid = time.substr(rand(10),-4);
    while (-e "./graph/".$jobid.".png" || -e "./data/".$jobid.".csv") {
        $jobid = time.substr(rand(10),-4);
    }


    require G::Tools::Statistics;    my $scaler = G::Tools::Statistics::mindex(@in0,%param);

    return SOAP::Data->type('string')->value($scaler);
}

sub peptide_mass{
    my $self = shift;
    my $in0 = shift;

    my %param = %{+shift};

    for ( keys %param ) {
        if ($param{$_} eq "") {delete $param{$_};}
        else {$param{"-$_"} = $param{$_};}
    }

    _set_sdb_path("/tmp/gb");

    G::Messenger::msg_interface("Inspire");
    my ($trpData,$trpError);
    G::Messenger::msg_term_console(sub{$trpData .= shift @_ });
    G::Messenger::msg_system_console(sub{$trpError .= shift @_ });

    my $jobid = time.substr(rand(10),-4);
    while (-e "./graph/".$jobid.".png" || -e "./data/".$jobid.".csv") {
        $jobid = time.substr(rand(10),-4);
    }

    require G::Seq::AminoAcid;    my $scaler = G::Seq::AminoAcid::peptide_mass($in0,%param);

    return SOAP::Data->type('string')->value($scaler);
}

sub consensus_z {
    my $self = shift;
    my @in0 = @{+shift};

    my %param = %{+shift};

    for ( keys %param ) {
        if ($param{$_} eq "") {delete $param{$_};}
        else {$param{"-$_"} = $param{$_};}
    }

    _set_sdb_path("/tmp/gb");

    G::Messenger::msg_interface("Inspire");
    my ($trpData,$trpError);
    G::Messenger::msg_term_console(sub{$trpData .= shift @_ });
    G::Messenger::msg_system_console(sub{$trpError .= shift @_ });

    my $jobid = time.substr(rand(10),-4);
    while (-e "./graph/".$jobid.".png" || -e "./data/".$jobid.".csv") {
        $jobid = time.substr(rand(10),-4);
    }

    require G::Seq::Consensus;
    my $scaler = q//;
    if ($param{-output} ne "f") {
        delete $param{-output};
	$scaler = G::Seq::Consensus::consensus_z(\@in0,%param,-output=>"g",-filename=>"$jobid.png");
    } else {
        delete $param{-output};
	$scaler = G::Seq::Consensus::consensus_z(\@in0,%param,-output=>"f",-filename=>"$jobid.csv");
    }

    $scaler = "http://soap.g-language.org/WS/result.cgi?jobid=$jobid";
    return SOAP::Data->type('string')->value($scaler);
}

sub genome_map{
    my $self = shift;
    my $in0 = shift;

    my %param = %{+shift};

    for ( keys %param ) {
        if ($param{$_} eq "") {delete $param{$_};}
        else {$param{"-$_"} = $param{$_};}
    }

    _set_sdb_path("/tmp/gb");

    G::Messenger::msg_interface("Inspire");
    my ($trpData,$trpError);
    G::Messenger::msg_term_console(sub{$trpData .= shift @_ });
    G::Messenger::msg_system_console(sub{$trpError .= shift @_ });

    my $jobid = time.substr(rand(10),-4);
    while (-e "./graph/".$jobid.".png" || -e "./data/".$jobid.".csv") {
        $jobid = time.substr(rand(10),-4);
    }

    if ($in0 ne "ecoli" && $in0 ne "bsub" && $in0 ne "mgen" && $in0 ne "cyano" && $in0 ne "pyro") {
        my $tmpfile = ( (time % 1296000)*10 + int(rand(10)) + 1048576);
        if (substr($in0,0,1) eq ">") {$tmpfile .= ".fasta";}
        open SEQ,">/tmp/gb/$tmpfile";print SEQ $in0;close SEQ;$in0 = "/tmp/gb/".$tmpfile;
    }

    $in0 = new G::IO($in0,"no msg");
    my $scaler = "";
    require G::Seq::GenomeMap;
    if ($param{-output} ne "f") {
        delete $param{-output};
        $scaler = G::Seq::GenomeMap::genome_map($in0,%param,-output=>"g",-filename=>"$jobid.png");
    } else {
        delete $param{-output};
        $scaler = G::Seq::GenomeMap::genome_map($in0,%param,-output=>"f",-filename=>"$jobid.csv");
    }

    $scaler = "http://soap.g-language.org/WS/result.cgi?jobid=$jobid";
    return SOAP::Data->type('string')->value($scaler);
}

sub longest_ORF{
    my $self = shift;
    my $in0 = shift;

    my %param = %{+shift};

    for ( keys %param ) {
        if ($param{$_} eq "") {delete $param{$_};}
        else {$param{"-$_"} = $param{$_};}
    }

    _set_sdb_path("/tmp/gb");

    G::Messenger::msg_interface("Inspire");
    my ($trpData,$trpError);
    G::Messenger::msg_term_console(sub{$trpData .= shift @_ });
    G::Messenger::msg_system_console(sub{$trpError .= shift @_ });

    my $jobid = time.substr(rand(10),-4);
    while (-e "./graph/".$jobid.".png" || -e "./data/".$jobid.".csv") {
        $jobid = time.substr(rand(10),-4);
    }


    require G::Seq::Util;    my $scaler = G::Seq::Util::longest_ORF($in0,%param);

    return SOAP::Data->type('string')->value($scaler);
}

sub rep_ori_ter{
    my $self = shift;
    my $in0 = shift;

    my %param = %{+shift};

    for ( keys %param ) {
        if ($param{$_} eq "") {delete $param{$_};}
        else {$param{"-$_"} = $param{$_};}
    }

    _set_sdb_path("/tmp/gb");

    G::Messenger::msg_interface("Inspire");
    my ($trpData,$trpError);
    G::Messenger::msg_term_console(sub{$trpData .= shift @_ });
    G::Messenger::msg_system_console(sub{$trpError .= shift @_ });

    my $jobid = time.substr(rand(10),-4);
    while (-e "./graph/".$jobid.".png" || -e "./data/".$jobid.".csv") {
        $jobid = time.substr(rand(10),-4);
    }

    if (length($in0) > 10) {
        my $tmpfile = ( (time % 1296000)*10 + int(rand(10)) + 1048576);
        if (substr($in0,0,1) eq ">") {$tmpfile .= ".fasta";}
        open SEQ,">/tmp/gb/$tmpfile";print SEQ $in0;close SEQ;$in0 = "/tmp/gb/".$tmpfile;
    }

    $in0 = new G::IO($in0,"no msg");
    require G::Seq::GCskew;    my @array = G::Seq::GCskew::rep_ori_ter($in0,%param);

    return SOAP::Data->type(array=>\@array);
}

sub calc_pI{
    my $self = shift;
    my $in0 = shift;

    my %param = %{+shift};

    for ( keys %param ) {
        if ($param{$_} eq "") {delete $param{$_};}
        else {$param{"-$_"} = $param{$_};}
    }

    _set_sdb_path("/tmp/gb");

    G::Messenger::msg_interface("Inspire");
    my ($trpData,$trpError);
    G::Messenger::msg_term_console(sub{$trpData .= shift @_ });
    G::Messenger::msg_system_console(sub{$trpError .= shift @_ });

    my $jobid = time.substr(rand(10),-4);
    while (-e "./graph/".$jobid.".png" || -e "./data/".$jobid.".csv") {
        $jobid = time.substr(rand(10),-4);
    }

    if ($in0 ne "ecoli" && $in0 ne "bsub" && $in0 ne "mgen" && $in0 ne "cyano" && $in0 ne "pyro") {
        my $tmpfile = ( (time % 1296000)*10 + int(rand(10)) + 1048576);
        if (substr($in0,0,1) eq ">") {$tmpfile .= ".fasta";}
        open SEQ,">/tmp/gb/$tmpfile";print SEQ $in0;close SEQ;$in0 = "/tmp/gb/".$tmpfile;
    }

    $in0 = new G::IO($in0,"no msg");
    require G::Seq::AminoAcid;    my $scaler = G::Seq::AminoAcid::calc_pI($in0,%param);

    return SOAP::Data->type('string')->value($scaler);
}

sub DoubleHelix{
    my $self = shift;
    my $in0 = shift;

    my %param = %{+shift};

    for ( keys %param ) {
        if ($param{$_} eq "") {delete $param{$_};}
        else {$param{"-$_"} = $param{$_};}
    }

    _set_sdb_path("/tmp/gb");

    G::Messenger::msg_interface("Inspire");
    my ($trpData,$trpError);
    G::Messenger::msg_term_console(sub{$trpData .= shift @_ });
    G::Messenger::msg_system_console(sub{$trpError .= shift @_ });

    my $jobid = time.substr(rand(10),-4);
    while (-e "./graph/".$jobid.".png" || -e "./data/".$jobid.".csv") {
        $jobid = time.substr(rand(10),-4);
    }

    if ($in0 ne "ecoli" && $in0 ne "bsub" && $in0 ne "mgen" && $in0 ne "cyano" && $in0 ne "pyro") {
        my $tmpfile = ( (time % 1296000)*10 + int(rand(10)) + 1048576);
        if (substr($in0,0,1) eq ">") {$tmpfile .= ".fasta";}
        open SEQ,">/tmp/gb/$tmpfile";print SEQ $in0;close SEQ;$in0 = "/tmp/gb/".$tmpfile;
    }

    $in0 = new G::IO($in0,"no msg");
    require G::Seq::Primitive;    my $scaler = G::Seq::Primitive::DoubleHelix($in0,%param);

    return SOAP::Data->type('string')->value($scaler);
}

sub base_entropy{
    my $self = shift;
    my $in0 = shift;

    my %param = %{+shift};

    for ( keys %param ) {
        if ($param{$_} eq "") {delete $param{$_};}
        else {$param{"-$_"} = $param{$_};}
    }

    _set_sdb_path("/tmp/gb");

    G::Messenger::msg_interface("Inspire");
    my ($trpData,$trpError);
    G::Messenger::msg_term_console(sub{$trpData .= shift @_ });
    G::Messenger::msg_system_console(sub{$trpError .= shift @_ });

    my $jobid = time.substr(rand(10),-4);
    while (-e "./graph/".$jobid.".png" || -e "./data/".$jobid.".csv") {
        $jobid = time.substr(rand(10),-4);
    }

    if ( length $in0 > 10 ) {
        my $tmpfile = ( (time % 1296000)*10 + int(rand(10)) + 1048576);
        if (substr($in0,0,1) eq ">") {$tmpfile .= ".fasta";}
        open SEQ,">/tmp/gb/$tmpfile";print SEQ $in0;close SEQ;$in0 = "/tmp/gb/".$tmpfile;
    }

    $in0 = new G::IO($in0,"no msg");
    my $scaler = "";
    require G::Seq::Consensus;
    if ($param{-output} ne "f") {
        delete $param{-output};
        $scaler = G::Seq::Consensus::base_entropy($in0,%param,-output=>"g",-filename=>"$jobid.png");
    } else {
        delete $param{-output};
        $scaler = G::Seq::Consensus::base_entropy($in0,%param,-output=>"f",-filename=>"$jobid.csv");
    }

    $scaler = "http://soap.g-language.org/WS/result.cgi?jobid=$jobid";
    return SOAP::Data->type('string')->value($scaler);
}

sub to_fasta{
    my $self = shift;
    my $in0 = shift;

    my %param = %{+shift};

    for ( keys %param ) {
        if ($param{$_} eq "") {delete $param{$_};}
        else {$param{"-$_"} = $param{$_};}
    }

    _set_sdb_path("/tmp/gb");

    G::Messenger::msg_interface("Inspire");
    my ($trpData,$trpError);
    G::Messenger::msg_term_console(sub{$trpData .= shift @_ });
    G::Messenger::msg_system_console(sub{$trpError .= shift @_ });

    my $jobid = time.substr(rand(10),-4);
    while (-e "./graph/".$jobid.".png" || -e "./data/".$jobid.".csv") {
        $jobid = time.substr(rand(10),-4);
    }


    require G::Seq::Primitive;    my $scaler = G::Seq::Primitive::to_fasta($in0,%param);

    return SOAP::Data->type('string')->value($scaler);
}

sub find_dif{
    my $self = shift;
    my $in0 = shift;

    my %param = %{+shift};

    for ( keys %param ) {
        if ($param{$_} eq "") {delete $param{$_};}
        else {$param{"-$_"} = $param{$_};}
    }

    _set_sdb_path("/tmp/gb");

    G::Messenger::msg_interface("Inspire");
    my ($trpData,$trpError);
    G::Messenger::msg_term_console(sub{$trpData .= shift @_ });
    G::Messenger::msg_system_console(sub{$trpError .= shift @_ });

    my $jobid = time.substr(rand(10),-4);
    while (-e "./graph/".$jobid.".png" || -e "./data/".$jobid.".csv") {
        $jobid = time.substr(rand(10),-4);
    }

    if ($in0 ne "ecoli" && $in0 ne "bsub" && $in0 ne "mgen" && $in0 ne "cyano" && $in0 ne "pyro") {
        my $tmpfile = ( (time % 1296000)*10 + int(rand(10)) + 1048576);
        if (substr($in0,0,1) eq ">") {$tmpfile .= ".fasta";}
        open SEQ,">/tmp/gb/$tmpfile";print SEQ $in0;close SEQ;$in0 = "/tmp/gb/".$tmpfile;
    }

    $in0 = new G::IO($in0,"no msg");
    require G::Seq::PatSearch;    my @array = G::Seq::PatSearch::find_dif($in0,%param);

    return SOAP::Data->type(array=>\@array);
}

sub cbi{
    my $self = shift;
    my $in0 = shift;

    my %param = %{+shift};

    for ( keys %param ) {
        if ($param{$_} eq "") {delete $param{$_};}
        else {$param{"-$_"} = $param{$_};}
    }

    if ( lc($param{"-id"}) eq 'all' ) {
        $param{"-id"} = "All";
    }

    _set_sdb_path("/tmp/gb");

    G::Messenger::msg_interface("Inspire");
    my ($trpData,$trpError);
    G::Messenger::msg_term_console(sub{$trpData .= shift @_ });
    G::Messenger::msg_system_console(sub{$trpError .= shift @_ });

    my $jobid = time.substr(rand(10),-4);
    while (-e "./graph/".$jobid.".png" || -e "./data/".$jobid.".csv") {
        $jobid = time.substr(rand(10),-4);
    }

    if ( length($in0) > 10 ) {
        my $tmpfile = ( (time % 1296000)*10 + int(rand(10)) + 1048576);
        if (substr($in0,0,1) eq ">") {$tmpfile .= ".fasta";}
        open SEQ,">/tmp/gb/$tmpfile";print SEQ $in0;close SEQ;$in0 = "/tmp/gb/".$tmpfile;
    }

    $in0 = new G::IO($in0,"no msg");
    require G::Seq::Codon;    my $scaler = G::Seq::Codon::cbi($in0,%param);

    return SOAP::Data->type('string')->value($scaler);
}

sub genes_from_ori{
    my $self = shift;
    my $in0 = shift;
    my $in1 = shift;

    my %param = %{+shift};

    for ( keys %param ) {
        if ($param{$_} eq "") {delete $param{$_};}
        else {$param{"-$_"} = $param{$_};}
    }

    _set_sdb_path("/tmp/gb");

    G::Messenger::msg_interface("Inspire");
    my ($trpData,$trpError);
    G::Messenger::msg_term_console(sub{$trpData .= shift @_ });
    G::Messenger::msg_system_console(sub{$trpError .= shift @_ });

    my $jobid = time.substr(rand(10),-4);
    while (-e "./graph/".$jobid.".png" || -e "./data/".$jobid.".csv") {
        $jobid = time.substr(rand(10),-4);
    }

    if ($in0 ne "ecoli" && $in0 ne "bsub" && $in0 ne "mgen" && $in0 ne "cyano" && $in0 ne "pyro") {
        my $tmpfile = ( (time % 1296000)*10 + int(rand(10)) + 1048576);
        if (substr($in0,0,1) eq ">") {$tmpfile .= ".fasta";}
        open SEQ,">/tmp/gb/$tmpfile";print SEQ $in0;close SEQ;$in0 = "/tmp/gb/".$tmpfile;
    }

    $in0 = new G::IO($in0,"no msg");
    require G::Seq::GCskew;    my @array = G::Seq::GCskew::genes_from_ori($in0,$in1,%param);

    return SOAP::Data->type(array=>\@array);
}

sub geneskew{
    my $self = shift;
    my $in0 = shift;

    my %param = %{+shift};

    for ( keys %param ) {
        if ($param{$_} eq "") {delete $param{$_};}
        else {$param{"-$_"} = $param{$_};}
    }

    _set_sdb_path("/tmp/gb");

    G::Messenger::msg_interface("Inspire");
    my ($trpData,$trpError);
    G::Messenger::msg_term_console(sub{$trpData .= shift @_ });
    G::Messenger::msg_system_console(sub{$trpError .= shift @_ });

    my $jobid = time.substr(rand(10),-4);
    while (-e "./graph/".$jobid.".png" || -e "./data/".$jobid.".csv") {
        $jobid = time.substr(rand(10),-4);
    }

    if ( length($in0) > 10 ) {
        my $tmpfile = ( (time % 1296000)*10 + int(rand(10)) + 1048576);
        if (substr($in0,0,1) eq ">") {$tmpfile .= ".fasta";}
        open SEQ,">/tmp/gb/$tmpfile";print SEQ $in0;close SEQ;$in0 = "/tmp/gb/".$tmpfile;
    }

    $in0 = new G::IO($in0,"no msg");

    require G::Seq::GCskew;
    if ($param{-output} ne "f") {
        delete $param{-output};
        G::Seq::GCskew::geneskew($in0,%param,-output=>"g",-filename=>"$jobid.png");
    } else {
        delete $param{-output};
        G::Seq::GCskew::geneskew($in0,%param,-output=>"f",-filename=>"$jobid.csv");
    }

    $scaler = "http://soap.g-language.org/WS/result.cgi?jobid=$jobid";
    return SOAP::Data->type('string')->value($scaler);
}

sub standard_deviation{
    my $self = shift;
    my @in0 = @{+shift};

    my %param = %{+shift};

    for ( keys %param ) {
        if ($param{$_} eq "") {delete $param{$_};}
        else {$param{"-$_"} = $param{$_};}
    }

    _set_sdb_path("/tmp/gb");

    G::Messenger::msg_interface("Inspire");
    my ($trpData,$trpError);
    G::Messenger::msg_term_console(sub{$trpData .= shift @_ });
    G::Messenger::msg_system_console(sub{$trpError .= shift @_ });

    my $jobid = time.substr(rand(10),-4);
    while (-e "./graph/".$jobid.".png" || -e "./data/".$jobid.".csv") {
        $jobid = time.substr(rand(10),-4);
    }


    require G::Tools::Statistics;    my $scaler = G::Tools::Statistics::standard_deviation(@in0,%param);

    return SOAP::Data->type('string')->value($scaler);
}

sub cor{
    my $self = shift;
    my @in0 = @{+shift};
    my @in1 = @{+shift};

    my %param = %{+shift};

    for ( keys %param ) {
        if ($param{$_} eq "") {delete $param{$_};}
        else {$param{"-$_"} = $param{$_};}
    }

    _set_sdb_path("/tmp/gb");

    G::Messenger::msg_interface("Inspire");
    my ($trpData,$trpError);
    G::Messenger::msg_term_console(sub{$trpData .= shift @_ });
    G::Messenger::msg_system_console(sub{$trpError .= shift @_ });

    my $jobid = time.substr(rand(10),-4);
    while (-e "./graph/".$jobid.".png" || -e "./data/".$jobid.".csv") {
        $jobid = time.substr(rand(10),-4);
    }


    require G::Tools::Statistics;    my @array = G::Tools::Statistics::cor(\@in0,\@in1,%param);

    return SOAP::Data->type(array=>\@array);
}

sub cumulative{
    my $self = shift;
    my @in0 = @{+shift};

    _set_sdb_path("/tmp/gb");

    G::Messenger::msg_interface("Inspire");
    my ($trpData,$trpError);
    G::Messenger::msg_term_console(sub{$trpData .= shift @_ });
    G::Messenger::msg_system_console(sub{$trpError .= shift @_ });

    my $jobid = time.substr(rand(10),-4);
    while (-e "./graph/".$jobid.".png" || -e "./data/".$jobid.".csv") {
        $jobid = time.substr(rand(10),-4);
    }


    require G::Tools::Statistics;    my @array = G::Tools::Statistics::cumulative(\@in0);

    return SOAP::Data->type(array=>\@array);
}

sub delta_enc{
    my $self = shift;
    my $in0 = shift;

    _set_sdb_path("/tmp/gb");

    G::Messenger::msg_interface("Inspire");
    my ($trpData,$trpError);
    G::Messenger::msg_term_console(sub{$trpData .= shift @_ });
    G::Messenger::msg_system_console(sub{$trpError .= shift @_ });

    my $jobid = time.substr(rand(10),-4);
    while (-e "./graph/".$jobid.".png" || -e "./data/".$jobid.".csv") {
        $jobid = time.substr(rand(10),-4);
    }

    if ( length $in0 > 10 ) {
        my $tmpfile = ( (time % 1296000)*10 + int(rand(10)) + 1048576);
        if (substr($in0,0,1) eq ">") {$tmpfile .= ".fasta";}
        open SEQ,">/tmp/gb/$tmpfile";print SEQ $in0;close SEQ;$in0 = "/tmp/gb/".$tmpfile;
    }

    $in0 = new G::IO($in0,"no msg");
    require G::Seq::Codon;  my $scaler = G::Seq::Codon::delta_enc($in0);

    return SOAP::Data->type('string')->value($scaler);
}

sub delta_gcskew{
    my $self = shift;
    my $in0 = shift;

    my %param = %{+shift};

    for ( keys %param ) {
        if ($param{$_} eq "") {delete $param{$_};}
        else {$param{"-$_"} = $param{$_};}
    }

    _set_sdb_path("/tmp/gb");

    G::Messenger::msg_interface("Inspire");
    my ($trpData,$trpError);
    G::Messenger::msg_term_console(sub{$trpData .= shift @_ });
    G::Messenger::msg_system_console(sub{$trpError .= shift @_ });

    my $jobid = time.substr(rand(10),-4);
    while (-e "./graph/".$jobid.".png" || -e "./data/".$jobid.".csv") {
        $jobid = time.substr(rand(10),-4);
    }

    if ( length $in0 > 10 ) {
        my $tmpfile = ( (time % 1296000)*10 + int(rand(10)) + 1048576);
        if (substr($in0,0,1) eq ">") {$tmpfile .= ".fasta";}
        open SEQ,">/tmp/gb/$tmpfile";print SEQ $in0;close SEQ;$in0 = "/tmp/gb/".$tmpfile;
    }

    $in0 = new G::IO($in0,"no msg");
    require G::Seq::GCskew;  my $scaler = G::Seq::GCskew::delta_gcskew($in0,%param);

    return SOAP::Data->type('string')->value($scaler);
}

sub molecular_weight{
    my $self = shift;
    my $in0 = shift;

    my %param = %{+shift};

    for ( keys %param ) {
        if ($param{$_} eq "") {delete $param{$_};}
        else {$param{"-$_"} = $param{$_};}
    }

    _set_sdb_path("/tmp/gb");

    G::Messenger::msg_interface("Inspire");
    my ($trpData,$trpError);
    G::Messenger::msg_term_console(sub{$trpData .= shift @_ });
    G::Messenger::msg_system_console(sub{$trpError .= shift @_ });

    my $jobid = time.substr(rand(10),-4);
    while (-e "./graph/".$jobid.".png" || -e "./data/".$jobid.".csv") {
        $jobid = time.substr(rand(10),-4);
    }


    require G::Seq::Util;    my $scaler = G::Seq::Util::molecular_weight($in0,%param);

    return SOAP::Data->type('string')->value($scaler);
}

sub gcskew{
    my $self = shift;
    my $in0 = shift;

    my %param = %{+shift};

    for ( keys %param ) {
        if ($param{$_} eq "") {delete $param{$_};}
        else {$param{"-$_"} = $param{$_};}
    }

    _set_sdb_path("/tmp/gb");

    G::Messenger::msg_interface("Inspire");
    my ($trpData,$trpError);
    G::Messenger::msg_term_console(sub{$trpData .= shift @_ });
    G::Messenger::msg_system_console(sub{$trpError .= shift @_ });

    my $jobid = time.substr(rand(10),-4);
    while (-e "./graph/".$jobid.".png" || -e "./data/".$jobid.".csv") {
        $jobid = time.substr(rand(10),-4);
    }

    if ( length($in0) > 10 ) {
        my $tmpfile = ( (time % 1296000)*10 + int(rand(10)) + 1048576);
        if (substr($in0,0,1) eq ">") {$tmpfile .= ".fasta";}
        open SEQ,">/tmp/gb/$tmpfile";print SEQ $in0;close SEQ;$in0 = "/tmp/gb/".$tmpfile;
    }

    $in0 = new G::IO($in0,"no msg");
    my $scaler = "";
    require G::Seq::GCskew;
    if ($param{-output} ne "f") {
        delete $param{-output};
        $scaler = G::Seq::GCskew::gcskew($in0,%param,-output=>"g",-filename=>"$jobid.png");
    } else {
        delete $param{-output};
        $scaler = G::Seq::GCskew::gcskew($in0,%param,-output=>"f",-filename=>"$jobid.csv");
    }

    $scaler = "http://soap.g-language.org/WS/result.cgi?jobid=$jobid";
    return SOAP::Data->type('string')->value($scaler);
}

sub genome_map3{
    my $self = shift;
    my $in0 = shift;

    my %param = %{+shift};

    for ( keys %param ) {
        if ($param{$_} eq "") {delete $param{$_};}
        else {$param{"-$_"} = $param{$_};}
    }

    _set_sdb_path("/tmp/gb");

    G::Messenger::msg_interface("Inspire");
    my ($trpData,$trpError);
    G::Messenger::msg_term_console(sub{$trpData .= shift @_ });
    G::Messenger::msg_system_console(sub{$trpError .= shift @_ });

    my $jobid = time.substr(rand(10),-4);
    while (-e "./graph/".$jobid.".png" || -e "./data/".$jobid.".csv") {
        $jobid = time.substr(rand(10),-4);
    }

    if (length($in0) > 10 ) {
        my $tmpfile = ( (time % 1296000)*10 + int(rand(10)) + 1048576);
        if (substr($in0,0,1) eq ">") {$tmpfile .= ".fasta";}
        open SEQ,">/tmp/gb/$tmpfile";print SEQ $in0;close SEQ;$in0 = "/tmp/gb/".$tmpfile;
    }

    $in0 = new G::IO($in0,"no msg");
    my $scaler = "";
    require G::Seq::GenomeMap;
    if ($param{-output} ne "f") {
        delete $param{-output};
        $scaler = G::Seq::GenomeMap::genome_map3($in0,%param,-output=>"g",-filename=>"$jobid.png");
    } else {
        delete $param{-output};
        $scaler = G::Seq::GenomeMap::genome_map3($in0,%param,-output=>"f",-filename=>"$jobid.csv");
    }

    $scaler = "http://soap.g-language.org/WS/result.cgi?jobid=$jobid";
    return SOAP::Data->type('string')->value($scaler);
}

sub seqinfo{
    my $self = shift;
    my $in0 = shift;

    my %param = %{+shift};

    for ( keys %param ) {
        if ($param{$_} eq "") {delete $param{$_};}
        else {$param{"-$_"} = $param{$_};}
    }

    _set_sdb_path("/tmp/gb");

    G::Messenger::msg_interface("Inspire");
    my ($trpData,$trpError);
    G::Messenger::msg_term_console(sub{$trpData .= shift @_ });
    G::Messenger::msg_system_console(sub{$trpError .= shift @_ });

    my $jobid = time.substr(rand(10),-4);
    while (-e "./graph/".$jobid.".png" || -e "./data/".$jobid.".csv") {
        $jobid = time.substr(rand(10),-4);
    }


    require G::Seq::Util;    my @array = G::Seq::Util::seqinfo($in0,%param);

    return SOAP::Data->type(array=>\@array);
}

sub signature{
    my $self = shift;
    my $in0 = shift;

    my %param = %{+shift};

    for ( keys %param ) {
        if ($param{$_} eq "") {delete $param{$_};}
        else {$param{"-$_"} = $param{$_};}
    }

    _set_sdb_path("/tmp/gb");

    G::Messenger::msg_interface("Inspire");
    my ($trpData,$trpError);
    G::Messenger::msg_term_console(sub{$trpData .= shift @_ });
    G::Messenger::msg_system_console(sub{$trpError .= shift @_ });

    my $jobid = time.substr(rand(10),-4);
    while (-e "./graph/".$jobid.".png" || -e "./data/".$jobid.".csv") {
        $jobid = time.substr(rand(10),-4);
    }

    if ( length($in0) > 10 ) {
        my $tmpfile = ( (time % 1296000)*10 + int(rand(10)) + 1048576);
        if (substr($in0,0,1) eq ">") {$tmpfile .= ".fasta";}
        open SEQ,">/tmp/gb/$tmpfile";print SEQ $in0;close SEQ;$in0 = "/tmp/gb/".$tmpfile;
    }

    $in0 = new G::IO($in0,"no msg");
    my $scaler = "";
    require G::Seq::PatSearch;
    $scaler = G::Seq::PatSearch::signature($in0,%param,-output=>"f",-filename=>"$jobid.csv");

    $scaler = "http://soap.g-language.org/WS/result.cgi?jobid=$jobid";
    return SOAP::Data->type('string')->value($scaler);
}

sub base_information_content{
    my $self = shift;
    my $in0  = shift;

    my %param = %{+shift};

    for ( keys %param ) {
        if ($param{$_} eq "") {delete $param{$_};}
        else {$param{"-$_"} = $param{$_};}
    }

    _set_sdb_path("/tmp/gb");

    G::Messenger::msg_interface("Inspire");
    my ($trpData,$trpError);
    G::Messenger::msg_term_console(sub{$trpData .= shift @_ });
    G::Messenger::msg_system_console(sub{$trpError .= shift @_ });

    my $jobid = time.substr(rand(10),-4);
    while (-e "./graph/".$jobid.".png" || -e "./data/".$jobid.".csv") {
        $jobid = time.substr(rand(10),-4);
    }

    if ( length($in0) > 10 ) {
        my $tmpfile = ( (time % 1296000)*10 + int(rand(10)) + 1048576);
        if (substr($in0,0,1) eq ">") {$tmpfile .= ".fasta";}
        open SEQ,">/tmp/gb/$tmpfile";print SEQ $in0;close SEQ;$in0 = "/tmp/gb/".$tmpfile;
    }

    $in0 = new G::IO($in0,"no msg");
    require G::Seq::Consensus;

    if ($param{-output} ne "f") {
        delete $param{-output};
        $scaler = G::Seq::Consensus::base_information_content($in0,%param,-output=>"g",-filename=>"$jobid.png");
    } else {
        delete $param{-output};
        $scaler = G::Seq::Consensus::base_information_content($in0,%param,-output=>"f",-filename=>"$jobid.csv");
    }

    $scaler = "http://soap.g-language.org/WS/result.cgi?jobid=$jobid";
    return SOAP::Data->type('string')->value($scaler);
}

sub dnawalk {
    my $self = shift;
    my $in0 = shift;

    my %param = %{+shift};

    for ( keys %param ) {
        if ($param{$_} eq "") {delete $param{$_};}
        else {$param{"-$_"} = $param{$_};}
    }

    _set_sdb_path("/tmp/gb");

    G::Messenger::msg_interface("Inspire");
    my ($trpData,$trpError);
    G::Messenger::msg_term_console(sub{$trpData .= shift @_ });
    G::Messenger::msg_system_console(sub{$trpError .= shift @_ });

    my $jobid = time.substr(rand(10),-4);
    while (-e "./graph/".$jobid.".png" || -e "./data/".$jobid.".csv") {
        $jobid = time.substr(rand(10),-4);
    }

    if ( length $in0 > 10 ) {
        my $tmpfile = ( (time % 1296000)*10 + int(rand(10)) + 1048576);
        if (substr($in0,0,1) eq ">") {$tmpfile .= ".fasta";}
        open SEQ,">/tmp/gb/$tmpfile";print SEQ $in0;close SEQ;$in0 = "/tmp/gb/".$tmpfile;
    }

    $in0 = new G::IO($in0,"no msg");
    my $scaler = "";
    require G::Seq::GenomeMap;
    if ($param{-output} ne "f") {
        delete $param{-output};
        $scaler = G::Seq::GenomeMap::dnawalk($in0,%param,-output=>"g",-filename=>"$jobid.png");
    } else {
        delete $param{-output};
        $scaler = G::Seq::GenomeMap::dnawalk($in0,%param,-output=>"f",-filename=>"$jobid.csv");
    }

    $scaler = "http://soap.g-language.org/WS/result.cgi?jobid=$jobid";
    return SOAP::Data->type('string')->value($scaler);
}

sub find_ter{
    my $self = shift;
    my $in0 = shift;

    my %param = %{+shift};

    for ( keys %param ) {
        if ($param{$_} eq "") {delete $param{$_};}
        else {$param{"-$_"} = $param{$_};}
    }

    _set_sdb_path("/tmp/gb");

    G::Messenger::msg_interface("Inspire");
    my ($trpData,$trpError);
    G::Messenger::msg_term_console(sub{$trpData .= shift @_ });
    G::Messenger::msg_system_console(sub{$trpError .= shift @_ });

    my $jobid = time.substr(rand(10),-4);
    while (-e "./graph/".$jobid.".png" || -e "./data/".$jobid.".csv") {
        $jobid = time.substr(rand(10),-4);
    }

    if ($in0 ne "ecoli" && $in0 ne "bsub" && $in0 ne "mgen" && $in0 ne "cyano" && $in0 ne "pyro") {
        my $tmpfile = ( (time % 1296000)*10 + int(rand(10)) + 1048576);
        if (substr($in0,0,1) eq ">") {$tmpfile .= ".fasta";}
        open SEQ,">/tmp/gb/$tmpfile";print SEQ $in0;close SEQ;$in0 = "/tmp/gb/".$tmpfile;
    }

    $in0 = new G::IO($in0,"no msg");
    require G::Seq::PatSearch;    my @array = G::Seq::PatSearch::find_ter($in0,%param);

    return SOAP::Data->type(array=>\@array);
}

sub shuffleseq{
    my $self = shift;
    my $in0 = shift;

    my %param = %{+shift};

    for ( keys %param ) {
        if ($param{$_} eq "") {delete $param{$_};}
        else {$param{"-$_"} = $param{$_};}
    }

    _set_sdb_path("/tmp/gb");

    G::Messenger::msg_interface("Inspire");
    my ($trpData,$trpError);
    G::Messenger::msg_term_console(sub{$trpData .= shift @_ });
    G::Messenger::msg_system_console(sub{$trpError .= shift @_ });

    my $jobid = time.substr(rand(10),-4);
    while (-e "./graph/".$jobid.".png" || -e "./data/".$jobid.".csv") {
        $jobid = time.substr(rand(10),-4);
    }


    require G::Seq::Primitive;    my $scaler = G::Seq::Primitive::shuffleseq($in0,%param);

    return SOAP::Data->type('string')->value($scaler);
}

sub oligomer_search{
    my $self = shift;
    my $in0 = shift;
    my $in1 = shift;

    my %param = %{+shift};

    for ( keys %param ) {
        if ($param{$_} eq "") {delete $param{$_};}
        else {$param{"-$_"} = $param{$_};}
    }

    _set_sdb_path("/tmp/gb");

    G::Messenger::msg_interface("Inspire");
    my ($trpData,$trpError);
    G::Messenger::msg_term_console(sub{$trpData .= shift @_ });
    G::Messenger::msg_system_console(sub{$trpError .= shift @_ });

    my $jobid = time.substr(rand(10),-4);
    while (-e "./graph/".$jobid.".png" || -e "./data/".$jobid.".csv") {
        $jobid = time.substr(rand(10),-4);
    }

    if ( length($in0) > 10 ) {
        my $tmpfile = ( (time % 1296000)*10 + int(rand(10)) + 1048576);
        if (substr($in0,0,1) eq ">") {$tmpfile .= ".fasta";}
        open SEQ,">/tmp/gb/$tmpfile";print SEQ $in0;close SEQ;$in0 = "/tmp/gb/".$tmpfile;
    }

    $in0 = new G::IO($in0,"no msg");
    require G::Seq::PatSearch;    my @array = G::Seq::PatSearch::oligomer_search($in0,$in1,%param);

    return SOAP::Data->type(array=>\@array);
}

sub find_pattern{
    my $self = shift;
    my $in0 = shift;
    my $in1 = shift;

    my %param = %{+shift};

    for ( keys %param ) {
        if ($param{$_} eq "") {delete $param{$_};}
        else {$param{"-$_"} = $param{$_};}
    }

    _set_sdb_path("/tmp/gb");

    G::Messenger::msg_interface("Inspire");
    my ($trpData,$trpError);
    G::Messenger::msg_term_console(sub{$trpData .= shift @_ });
    G::Messenger::msg_system_console(sub{$trpError .= shift @_ });

    my $jobid = time.substr(rand(10),-4);
    while (-e "./graph/".$jobid.".png" || -e "./data/".$jobid.".csv") {
        $jobid = time.substr(rand(10),-4);
    }

    if ($in0 ne "ecoli" && $in0 ne "bsub" && $in0 ne "mgen" && $in0 ne "cyano" && $in0 ne "pyro") {
        my $tmpfile = ( (time % 1296000)*10 + int(rand(10)) + 1048576);
        if (substr($in0,0,1) eq ">") {$tmpfile .= ".fasta";}
        open SEQ,">/tmp/gb/$tmpfile";print SEQ $in0;close SEQ;$in0 = "/tmp/gb/".$tmpfile;
    }

    $in0 = new G::IO($in0,"no msg");
    require G::Seq::PatSearch;    my @array = G::Seq::PatSearch::find_pattern($in0,$in1,%param);

    return SOAP::Data->type(array=>\@array);
}

sub gcwin{
    my $self = shift;
    my $in0 = shift;

    my %param = %{+shift};

    for ( keys %param ) {
        if ($param{$_} eq "") {delete $param{$_};}
        else {$param{"-$_"} = $param{$_};}
    }

    _set_sdb_path("/tmp/gb");

    G::Messenger::msg_interface("Inspire");
    my ($trpData,$trpError);
    G::Messenger::msg_term_console(sub{$trpData .= shift @_ });
    G::Messenger::msg_system_console(sub{$trpError .= shift @_ });

    my $jobid = time.substr(rand(10),-4);
    while (-e "./graph/".$jobid.".png" || -e "./data/".$jobid.".csv") {
        $jobid = time.substr(rand(10),-4);
    }

    if ( length($in0) > 10 ) {
        my $tmpfile = ( (time % 1296000)*10 + int(rand(10)) + 1048576);
        if (substr($in0,0,1) eq ">") {$tmpfile .= ".fasta";}
        open SEQ,">/tmp/gb/$tmpfile";print SEQ $in0;close SEQ;$in0 = "/tmp/gb/".$tmpfile;
    }

    $in0 = new G::IO($in0,"no msg");
    my $scaler = "";
    require G::Seq::GCskew;
    if ($param{-output} ne "f") {
        delete $param{-output};
        $scaler = G::Seq::GCskew::gcwin($in0,%param,-output=>"g",-filename=>"$jobid.png");
    } else {
        delete $param{-output};
        $scaler = G::Seq::GCskew::gcwin($in0,%param,-output=>"f",-filename=>"$jobid.csv");
    }

    $scaler = "http://soap.g-language.org/WS/result.cgi?jobid=$jobid";
    return SOAP::Data->type('string')->value($scaler);
}

sub oligomer_counter{
    my $self = shift;
    my $in0 = shift;
    my $in1 = shift;

    my %param = %{+shift};

    for ( keys %param ) {
        if ($param{$_} eq "") {delete $param{$_};}
        else {$param{"-$_"} = $param{$_};}
    }

    _set_sdb_path("/tmp/gb");

    G::Messenger::msg_interface("Inspire");
    my ($trpData,$trpError);
    G::Messenger::msg_term_console(sub{$trpData .= shift @_ });
    G::Messenger::msg_system_console(sub{$trpError .= shift @_ });

    my $jobid = time.substr(rand(10),-4);
    while (-e "./graph/".$jobid.".png" || -e "./data/".$jobid.".csv") {
        $jobid = time.substr(rand(10),-4);
    }

    if ( length($in0) > 10 ) {
        my $tmpfile = ( (time % 1296000)*10 + int(rand(10)) + 1048576);
        if (substr($in0,0,1) eq ">") {$tmpfile .= ".fasta";}
        open SEQ,">/tmp/gb/$tmpfile";print SEQ $in0;close SEQ;$in0 = "/tmp/gb/".$tmpfile;
    }

    $in0 = new G::IO($in0,"no msg");

    require G::Seq::PatSearch;
    my $scaler = G::Seq::PatSearch::oligomer_counter($in0,$in1,%param);

    return SOAP::Data->type('string')->value($scaler);
}

sub codon_usage{
    my $self = shift;
    my $in0 = shift;

    my %param = %{+shift};

    for ( keys %param ) {
        if ($param{$_} eq "") {delete $param{$_};}
        else {$param{"-$_"} = $param{$_};}
    }

    _set_sdb_path("/tmp/gb");

    G::Messenger::msg_interface("Inspire");
    my ($trpData,$trpError);
    G::Messenger::msg_term_console(sub{$trpData .= shift @_ });
    G::Messenger::msg_system_console(sub{$trpError .= shift @_ });

    my $jobid = time.substr(rand(10),-4);
    while (-e "./graph/".$jobid.".png" || -e "./data/".$jobid.".csv") {
        $jobid = time.substr(rand(10),-4);
    }

    if ($in0 ne "ecoli" && $in0 ne "bsub" && $in0 ne "mgen" && $in0 ne "cyano" && $in0 ne "pyro") {
        my $tmpfile = ( (time % 1296000)*10 + int(rand(10)) + 1048576);
        if (substr($in0,0,1) eq ">") {$tmpfile .= ".fasta";}
        open SEQ,">/tmp/gb/$tmpfile";print SEQ $in0;close SEQ;$in0 = "/tmp/gb/".$tmpfile;
    }

    $in0 = new G::IO($in0,"no msg");
    my $scaler = "";
    require G::Seq::Codon;
    if ($param{-output} ne "f") {
        delete $param{-output};
        $scaler = G::Seq::Codon::codon_usage($in0,%param,-output=>"g",-filename=>"$jobid.png");
    } else {
        delete $param{-output};
        $scaler = G::Seq::Codon::codon_usage($in0,%param,-output=>"f",-filename=>"$jobid.csv");
    }

    $scaler = "http://soap.g-language.org/WS/result.cgi?jobid=$jobid";
    return SOAP::Data->type('string')->value($scaler);
}

sub min{
    my $self = shift;
    my @in0 = @{+shift};

    my %param = %{+shift};

    for ( keys %param ) {
        if ($param{$_} eq "") {delete $param{$_};}
        else {$param{"-$_"} = $param{$_};}
    }

    _set_sdb_path("/tmp/gb");

    G::Messenger::msg_interface("Inspire");
    my ($trpData,$trpError);
    G::Messenger::msg_term_console(sub{$trpData .= shift @_ });
    G::Messenger::msg_system_console(sub{$trpError .= shift @_ });

    my $jobid = time.substr(rand(10),-4);
    while (-e "./graph/".$jobid.".png" || -e "./data/".$jobid.".csv") {
        $jobid = time.substr(rand(10),-4);
    }


    require G::Tools::Statistics;    my $scaler = G::Tools::Statistics::min(@in0,%param);

    return SOAP::Data->type('string')->value($scaler);
}

sub find_iteron{
    my $self = shift;
    my $in0 = shift;

    my %param = %{+shift};

    for ( keys %param ) {
        if ($param{$_} eq "") {delete $param{$_};}
        else {$param{"-$_"} = $param{$_};}
    }

    _set_sdb_path("/tmp/gb");

    G::Messenger::msg_interface("Inspire");
    my ($trpData,$trpError);
    G::Messenger::msg_term_console(sub{$trpData .= shift @_ });
    G::Messenger::msg_system_console(sub{$trpError .= shift @_ });

    my $jobid = time.substr(rand(10),-4);
    while (-e "./graph/".$jobid.".png" || -e "./data/".$jobid.".csv") {
        $jobid = time.substr(rand(10),-4);
    }

    if ($in0 ne "ecoli" && $in0 ne "bsub" && $in0 ne "mgen" && $in0 ne "cyano" && $in0 ne "pyro") {
        my $tmpfile = ( (time % 1296000)*10 + int(rand(10)) + 1048576);
        if (substr($in0,0,1) eq ">") {$tmpfile .= ".fasta";}
        open SEQ,">/tmp/gb/$tmpfile";print SEQ $in0;close SEQ;$in0 = "/tmp/gb/".$tmpfile;
    }

    $in0 = new G::IO($in0,"no msg");
    require G::Seq::PatSearch;    my @array = G::Seq::PatSearch::find_iteron($in0,%param);

    return SOAP::Data->type(array=>\@array);
}

sub complement{
    my $self = shift;
    my $in0 = shift;

    my %param = %{+shift};

    for ( keys %param ) {
        if ($param{$_} eq "") {delete $param{$_};}
        else {$param{"-$_"} = $param{$_};}
    }

    _set_sdb_path("/tmp/gb");

    G::Messenger::msg_interface("Inspire");
    my ($trpData,$trpError);
    G::Messenger::msg_term_console(sub{$trpData .= shift @_ });
    G::Messenger::msg_system_console(sub{$trpError .= shift @_ });

    my $jobid = time.substr(rand(10),-4);
    while (-e "./graph/".$jobid.".png" || -e "./data/".$jobid.".csv") {
        $jobid = time.substr(rand(10),-4);
    }


    require G;    my $scaler = G::complement($in0,%param);

    return SOAP::Data->type('string')->value($scaler);
}

sub mean{
    my $self = shift;
    my @in0 = @{+shift};

    my %param = %{+shift};

    for ( keys %param ) {
        if ($param{$_} eq "") {delete $param{$_};}
        else {$param{"-$_"} = $param{$_};}
    }

    _set_sdb_path("/tmp/gb");

    G::Messenger::msg_interface("Inspire");
    my ($trpData,$trpError);
    G::Messenger::msg_term_console(sub{$trpData .= shift @_ });
    G::Messenger::msg_system_console(sub{$trpError .= shift @_ });

    my $jobid = time.substr(rand(10),-4);
    while (-e "./graph/".$jobid.".png" || -e "./data/".$jobid.".csv") {
        $jobid = time.substr(rand(10),-4);
    }


    require G::Tools::Statistics;    my $scaler = G::Tools::Statistics::mean(@in0,%param);

    return SOAP::Data->type('string')->value($scaler);
}

sub codon_counter{
    my $self = shift;
    my $in0 = shift;

    my %param = %{+shift};

    for ( keys %param ) {
        if ($param{$_} eq "") {delete $param{$_};}
        else {$param{"-$_"} = $param{$_};}
    }

    _set_sdb_path("/tmp/gb");

    G::Messenger::msg_interface("Inspire");
    my ($trpData,$trpError);
    G::Messenger::msg_term_console(sub{$trpData .= shift @_ });
    G::Messenger::msg_system_console(sub{$trpError .= shift @_ });

    my $jobid = time.substr(rand(10),-4);
    while (-e "./graph/".$jobid.".png" || -e "./data/".$jobid.".csv") {
        $jobid = time.substr(rand(10),-4);
    }

    if ($in0 ne "ecoli" && $in0 ne "bsub" && $in0 ne "mgen" && $in0 ne "cyano" && $in0 ne "pyro") {
        my $tmpfile = ( (time % 1296000)*10 + int(rand(10)) + 1048576);
        if (substr($in0,0,1) eq ">") {$tmpfile .= ".fasta";}
        open SEQ,">/tmp/gb/$tmpfile";print SEQ $in0;close SEQ;$in0 = "/tmp/gb/".$tmpfile;
    }

    $in0 = new G::IO($in0,"no msg");
    require G::Seq::Codon;
    my $scaler = G::Seq::Codon::codon_counter($in0,%param,-output=>"f",-filename=>"$jobid.csv");

    $scaler = "http://soap.g-language.org/WS/result.cgi?jobid=$jobid";
    return SOAP::Data->type('string')->value($scaler);
}

sub entrez{
    my $self = shift;
    my $in0 = shift;
    my $in1 = shift;

    my %param = %{+shift};

    for ( keys %param ) {
        if ($param{$_} eq "") {delete $param{$_};}
        else {$param{"-$_"} = $param{$_};}
    }

    _set_sdb_path("/tmp/gb");

    G::Messenger::msg_interface("Inspire");
    my ($trpData,$trpError);
    G::Messenger::msg_term_console(sub{$trpData .= shift @_ });
    G::Messenger::msg_system_console(sub{$trpError .= shift @_ });

    my $jobid = time.substr(rand(10),-4);
    while (-e "./graph/".$jobid.".png" || -e "./data/".$jobid.".csv") {
        $jobid = time.substr(rand(10),-4);
    }

    my $stdout;

    open TMPOUT, '>&STDOUT';
    close STDOUT;
    open STDOUT, '>', \$stdout;

    require G::Shell::EUtils;    my $scaler = G::Shell::EUtils::entrez($in0,$in1,%param);

    close STDOUT;
    open STDOUT, '>&TMPOUT';
    close TMPOUT;

    return SOAP::Data->type('string')->value($stdout);
}

sub palindrome{
    my $self = shift;
    my $in0 = shift;

    my %param = %{+shift};

    for ( keys %param ) {
        if ($param{$_} eq "") {delete $param{$_};}
        else {$param{"-$_"} = $param{$_};}
    }

    _set_sdb_path("/tmp/gb");

    G::Messenger::msg_interface("Inspire");
    my ($trpData,$trpError);
    G::Messenger::msg_term_console(sub{$trpData .= shift @_ });
    G::Messenger::msg_system_console(sub{$trpError .= shift @_ });

    my $jobid = time.substr(rand(10),-4);
    while (-e "./graph/".$jobid.".png" || -e "./data/".$jobid.".csv") {
        $jobid = time.substr(rand(10),-4);
    }

    if ( length($in0) > 10 ) {
        my $tmpfile = ( (time % 1296000)*10 + int(rand(10)) + 1048576);
        if (substr($in0,0,1) eq ">") {$tmpfile .= ".fasta";}
        open SEQ,">/tmp/gb/$tmpfile";print SEQ $in0;close SEQ;$in0 = "/tmp/gb/".$tmpfile;
    }

    $in0 = new G::IO($in0,"no msg");

    require G::Seq::PatSearch;
    delete $param{-output};
    G::Seq::PatSearch::palindrome($in0,%param,-output=>"f",-filename=>"./data/$jobid.csv");

    my $scaler = "http://soap.g-language.org/WS/result.cgi?jobid=$jobid";
    return SOAP::Data->type('string')->value($scaler);
}

sub least_squares_fit{
    my $self = shift;
    my @in0 = @{+shift};

    my %param = %{+shift};

    for ( keys %param ) {
        if ($param{$_} eq "") {delete $param{$_};}
        else {$param{"-$_"} = $param{$_};}
    }

    _set_sdb_path("/tmp/gb");

    G::Messenger::msg_interface("Inspire");
    my ($trpData,$trpError);
    G::Messenger::msg_term_console(sub{$trpData .= shift @_ });
    G::Messenger::msg_system_console(sub{$trpError .= shift @_ });

    my $jobid = time.substr(rand(10),-4);
    while (-e "./graph/".$jobid.".png" || -e "./data/".$jobid.".csv") {
        $jobid = time.substr(rand(10),-4);
    }


    require G::Tools::Statistics;    my @array = G::Tools::Statistics::least_squares_fit(@in0,%param);

    return SOAP::Data->type(array=>\@array);
}

sub dinuc{
    my $self = shift;
    my $in0 = shift;

    my %param = %{+shift};

    for ( keys %param ) {
        if ($param{$_} eq "") {delete $param{$_};}
        else {$param{"-$_"} = $param{$_};}
    }

    _set_sdb_path("/tmp/gb");

    G::Messenger::msg_interface("Inspire");
    my ($trpData,$trpError);
    G::Messenger::msg_term_console(sub{$trpData .= shift @_ });
    G::Messenger::msg_system_console(sub{$trpError .= shift @_ });

    my $jobid = time.substr(rand(10),-4);
    while (-e "./graph/".$jobid.".png" || -e "./data/".$jobid.".csv") {
        $jobid = time.substr(rand(10),-4);
    }

    if ( length $in0 > 10 ) {
        my $tmpfile = ( (time % 1296000)*10 + int(rand(10)) + 1048576);
        if (substr($in0,0,1) eq ">") {$tmpfile .= ".fasta";}
        open SEQ,">/tmp/gb/$tmpfile";print SEQ $in0;close SEQ;$in0 = "/tmp/gb/".$tmpfile;
    }

    $in0 = new G::IO($in0,"no msg");
    require G::Seq::Codon;
    my $scaler = G::Seq::Codon::dinuc($in0,%param,-output=>"f",-filename=>"$jobid.csv");

    $scaler = "http://soap.g-language.org/WS/result.cgi?jobid=$jobid";
    return SOAP::Data->type('string')->value($scaler);
}

sub help{
    my $self    = shift;
    my $keyword = shift;

    _set_sdb_path("/tmp/gb");

    G::Messenger::msg_interface("Inspire");
    my ($trpData,$trpError);
    G::Messenger::msg_term_console(sub{$trpData .= shift @_ });
    G::Messenger::msg_system_console(sub{$trpError .= shift @_ });

    require G::Shell::Help;

    if ($keyword =~ m/(-\w+)\s+(.+)/) {
	my $in0 = $1;
	my $in1 = $2;
	if ($in0 eq '-s' || $in0 eq '-g' || $in0 eq '-bp' || $in0 eq '-w') {
	    G::Shell::Help::help($in0,$in1);
	} else {
	    G::Shell::Help::help($keyword);
	}
    } elsif ($keyword eq 'me') {
        $trpData = "       Relax, strech yourself, and take a deep breath :-)\n";
    } elsif ($keyword eq '!') {
        $trpData = "       I need somebody~ not just anybody~\n";
    } else {
        G::Shell::Help::help($keyword);
    }

    return $trpData;
}

sub hydropathy {
    my $self = shift;
    my $in0  = shift;

    _set_sdb_path("/tmp/gb");

    G::Messenger::msg_interface("Inspire");
    my ($trpData,$trpError);
    G::Messenger::msg_term_console(sub{$trpData .= shift @_ });
    G::Messenger::msg_system_console(sub{$trpError .= shift @_ });

    return G::Seq::AminoAcid::hydropathy($in0);
}

sub cgr{
    my $self = shift;
    my $in0 = shift;

    my %param = %{+shift};

    for ( keys %param ) {
        if ($param{$_} eq "") {delete $param{$_};}
        else {$param{"-$_"} = $param{$_};}
    }

    _set_sdb_path("/tmp/gb");

    G::Messenger::msg_interface("Inspire");
    my ($trpData,$trpError);
    G::Messenger::msg_term_console(sub{$trpData .= shift @_ });
    G::Messenger::msg_system_console(sub{$trpError .= shift @_ });

    my $jobid = time.substr(rand(10),-4);
    while (-e "./graph/".$jobid.".png" || -e "./data/".$jobid.".csv") {
        $jobid = time.substr(rand(10),-4);
    }

    if ($in0 ne "ecoli" && $in0 ne "bsub" && $in0 ne "mgen" && $in0 ne "cyano" && $in0 ne "pyro") {
        my $tmpfile = ( (time % 1296000)*10 + int(rand(10)) + 1048576);
        if (substr($in0,0,1) eq ">") {$tmpfile .= ".fasta";}
        open SEQ,">/tmp/gb/$tmpfile";print SEQ $in0;close SEQ;$in0 = "/tmp/gb/".$tmpfile;
    }

    $in0 = new G::IO($in0,"no msg");
    require G::Seq::PatSearch;

    delete $param{-output};
    G::Seq::PatSearch::cgr($in0,%param,-output=>"g",-filename=>"$jobid.png");

    my $scaler = "http://soap.g-language.org/WS/result.cgi?jobid=$jobid";
    return SOAP::Data->type('string')->value($scaler);
}

sub B1 {
    my $self = shift;
    my $in0 = shift;

    my %param = %{+shift};

    for ( keys %param ) {
        if ($param{$_} eq "") {delete $param{$_};}
        else {$param{"-$_"} = $param{$_};}
    }

    _set_sdb_path("/tmp/gb");

    G::Messenger::msg_interface("Inspire");
    my ($trpData,$trpError);
    G::Messenger::msg_term_console(sub{$trpData .= shift @_ });
    G::Messenger::msg_system_console(sub{$trpError .= shift @_ });

    if ( length $in0 > 10 ) {
        my $tmpfile = ( (time % 1296000)*10 + int(rand(10)) + 1048576);
        if (substr($in0,0,1) eq ">") {$tmpfile .= ".fasta";}
        open SEQ,">/tmp/gb/$tmpfile";print SEQ $in0;close SEQ;$in0 = "/tmp/gb/".$tmpfile;
    }

    $in0 = new G::IO($in0,"no msg");
    require G::Seq::GCskew;

    return G::Seq::GCskew::B1($in0,%param);
}

sub B2 {
    my $self = shift;
    my $in0 = shift;

    my %param = %{+shift};

    for ( keys %param ) {
        if ($param{$_} eq "") {delete $param{$_};}
        else {$param{"-$_"} = $param{$_};}
    }

    _set_sdb_path("/tmp/gb");

    G::Messenger::msg_interface("Inspire");
    my ($trpData,$trpError);
    G::Messenger::msg_term_console(sub{$trpData .= shift @_ });
    G::Messenger::msg_system_console(sub{$trpError .= shift @_ });

    if ( length $in0 > 10 ) {
        my $tmpfile = ( (time % 1296000)*10 + int(rand(10)) + 1048576);
        if (substr($in0,0,1) eq ">") {$tmpfile .= ".fasta";}
        open SEQ,">/tmp/gb/$tmpfile";print SEQ $in0;close SEQ;$in0 = "/tmp/gb/".$tmpfile;
    }

    $in0 = new G::IO($in0,'no msg');
    require G::Seq::GCskew;

    return G::Seq::GCskew::B2($in0,%param);
}

sub base_counter {
    my $self = shift;
    my $in0 = shift;

    my %param = %{+shift};

    for ( keys %param ) {
        if ($param{$_} eq "") {delete $param{$_};}
        else {$param{"-$_"} = $param{$_};}
    }

    _set_sdb_path("/tmp/gb");

    G::Messenger::msg_interface("Inspire");
    my ($trpData,$trpError);
    G::Messenger::msg_term_console(sub{$trpData .= shift @_ });
    G::Messenger::msg_system_console(sub{$trpError .= shift @_ });

    my $jobid = time.substr(rand(10),-4);
    while (-e "./graph/".$jobid.".png" || -e "./data/".$jobid.".csv") {
        $jobid = time.substr(rand(10),-4);
    }

    if ( length $in0 > 10 ) {
        my $tmpfile = ( (time % 1296000)*10 + int(rand(10)) + 1048576);
        if (substr($in0,0,1) eq ">") {$tmpfile .= ".fasta";}
        open SEQ,">/tmp/gb/$tmpfile";print SEQ $in0;close SEQ;$in0 = "/tmp/gb/".$tmpfile;
    }

    $in0 = new G::IO($in0,"no msg");
    require G::Seq::Consensus;

    delete $param{-output};
    G::Seq::Consensus::base_counter($in0,%param,-output=>"f",-filename=>"$jobid.csv");

    my $scaler = "http://soap.g-language.org/WS/result.cgi?jobid=$jobid";
    return SOAP::Data->type('string')->value($scaler);
}

sub base_z_value {
    my $self = shift;
    my $in0 = shift;

    my %param = %{+shift};

    for ( keys %param ) {
        if ($param{$_} eq "") {delete $param{$_};}
        else {$param{"-$_"} = $param{$_};}
    }

    _set_sdb_path("/tmp/gb");

    G::Messenger::msg_interface("Inspire");
    my ($trpData,$trpError);
    G::Messenger::msg_term_console(sub{$trpData .= shift @_ });
    G::Messenger::msg_system_console(sub{$trpError .= shift @_ });

    my $jobid = time.substr(rand(10),-4);
    while (-e "./graph/".$jobid.".png" || -e "./data/".$jobid.".csv") {
        $jobid = time.substr(rand(10),-4);
    }

    if ( length $in0 > 10 ) {
        my $tmpfile = ( (time % 1296000)*10 + int(rand(10)) + 1048576);
        if (substr($in0,0,1) eq ">") {$tmpfile .= ".fasta";}
        open SEQ,">/tmp/gb/$tmpfile";print SEQ $in0;close SEQ;$in0 = "/tmp/gb/".$tmpfile;
    }

    $in0 = new G::IO($in0,"no msg");
    require G::Seq::Consensus;

    delete $param{-output};
    G::Seq::Consensus::base_z_value($in0,%param,-output=>"f",-filename=>"$jobid.csv");

    my $scaler = "http://soap.g-language.org/WS/result.cgi?jobid=$jobid";
    return SOAP::Data->type('string')->value($scaler);
}

sub kmer_table {
    my $self = shift;
    my $in0 = shift;

    my %param = %{+shift};

    for ( keys %param ) {
        if ($param{$_} eq "") {delete $param{$_};}
        else {$param{"-$_"} = $param{$_};}
    }

    _set_sdb_path("/tmp/gb");

    G::Messenger::msg_interface("Inspire");
    my ($trpData,$trpError);
    G::Messenger::msg_term_console(sub{$trpData .= shift @_ });
    G::Messenger::msg_system_console(sub{$trpError .= shift @_ });

    my $jobid = time.substr(rand(10),-4);
    while (-e "./graph/".$jobid.".png" || -e "./data/".$jobid.".csv") {
        $jobid = time.substr(rand(10),-4);
    }

    if ( length($in0) > 10 ) {
        my $tmpfile = ( (time % 1296000)*10 + int(rand(10)) + 1048576);
        if (substr($in0,0,1) eq ">") {$tmpfile .= ".fasta";}
        open SEQ,">/tmp/gb/$tmpfile";print SEQ $in0;close SEQ;$in0 = "/tmp/gb/".$tmpfile;
    }

    $in0 = new G::IO($in0,"no msg");
    require G::Seq::PatSearch;

    delete $param{-output};
    G::Seq::PatSearch::kmer_table($in0,%param,-output=>"g",-filename=>"$jobid.png");

    my $scaler = "http://soap.g-language.org/WS/result.cgi?jobid=$jobid";
    return SOAP::Data->type('string')->value($scaler);
}

sub lda_bias {
    my $self = shift;
    my $in0 = shift;

    my %param = %{+shift};

    for ( keys %param ) {
        if ($param{$_} eq "") {delete $param{$_};}
        else {$param{"-$_"} = $param{$_};}
    }

    _set_sdb_path("/tmp/gb");

    G::Messenger::msg_interface("Inspire");
    my ($trpData,$trpError);
    G::Messenger::msg_term_console(sub{$trpData .= shift @_ });
    G::Messenger::msg_system_console(sub{$trpError .= shift @_ });

    if ( length($in0) > 10 ) {
        my $tmpfile = ( (time % 1296000)*10 + int(rand(10)) + 1048576);
        if (substr($in0,0,1) eq ">") {$tmpfile .= ".fasta";}
        open SEQ,">/tmp/gb/$tmpfile";print SEQ $in0;close SEQ;$in0 = "/tmp/gb/".$tmpfile;
    }

    $in0 = new G::IO($in0,"no msg");
    require G::Seq::GCskew;

    return G::Seq::GCskew::lda_bias($in0,%param);
}

sub scs {
    my $self = shift;
    my $in0 = shift;

    my %param = %{+shift};

    for ( keys %param ) {
        if ($param{$_} eq "") {delete $param{$_};}
        else {$param{"-$_"} = $param{$_};}
    }

    _set_sdb_path("/tmp/gb");

    G::Messenger::msg_interface("Inspire");
    my ($trpData,$trpError);
    G::Messenger::msg_term_console(sub{$trpData .= shift @_ });
    G::Messenger::msg_system_console(sub{$trpError .= shift @_ });

    my $jobid = time.substr(rand(10),-4);
    while (-e "./graph/".$jobid.".png" || -e "./data/".$jobid.".csv") {
        $jobid = time.substr(rand(10),-4);
    }

    if ( length($in0) > 10 ) {
        my $tmpfile = ( (time % 1296000)*10 + int(rand(10)) + 1048576);
        if (substr($in0,0,1) eq ">") {$tmpfile .= ".fasta";}
        open SEQ,">/tmp/gb/$tmpfile";print SEQ $in0;close SEQ;$in0 = "/tmp/gb/".$tmpfile;
    }

    $in0 = new G::IO($in0,"no msg");
    my $scaler = "";

    require G::Seq::Codon;
    $scaler = G::Seq::Codon::scs($in0,%param,-output=>"f",-filename=>"$jobid.csv");

    return SOAP::Data->type('string')->value($scaler);
}

sub leading_strand {
    my $self = shift;
    my $in0 = shift;

    _set_sdb_path("/tmp/gb");

    G::Messenger::msg_interface("Inspire");
    my ($trpData,$trpError);
    G::Messenger::msg_term_console(sub{$trpData .= shift @_ });
    G::Messenger::msg_system_console(sub{$trpError .= shift @_ });

    my $jobid = time.substr(rand(10),-4);
    while (-e "./graph/".$jobid.".png" || -e "./data/".$jobid.".csv") {
        $jobid = time.substr(rand(10),-4);
    }

    if ( length($in0) > 10 ) {
        my $tmpfile = ( (time % 1296000)*10 + int(rand(10)) + 1048576);
        if (substr($in0,0,1) eq ">") {$tmpfile .= ".fasta";}
        open SEQ,">/tmp/gb/$tmpfile";print SEQ $in0;close SEQ;$in0 = "/tmp/gb/".$tmpfile;
    }

    $in0 = new G::IO($in0,"no msg");
    require G::Seq::GCskew;    my @array = G::Seq::GCskew::leading_strand($in0);

    return SOAP::Data->type(array=>\@array);
}

sub S_value{
    my $self = shift;
    my $in0 = shift;

    my %param = %{+shift};

    for ( keys %param ) {
        if ($param{$_} eq "") {delete $param{$_};}
        else {$param{"-$_"} = $param{$_};}
    }

    _set_sdb_path("/tmp/gb");

    G::Messenger::msg_interface("Inspire");
    my ($trpData,$trpError);
    G::Messenger::msg_term_console(sub{$trpData .= shift @_ });
    G::Messenger::msg_system_console(sub{$trpError .= shift @_ });

    my $jobid = time.substr(rand(10),-4);
    while (-e './graph/'.$jobid.'.png' || -e './data/'.$jobid.'.csv') {
        $jobid = time.substr(rand(10),-4);
    }

    if ( length($in0) > 10 ) {
        my $tmpfile = ( (time % 1296000)*10 + int(rand(10)) + 1048576);
        if (substr($in0,0,1) eq '>') {$tmpfile .= '.fasta';}
        open SEQ,">/tmp/gb/$tmpfile";print SEQ $in0;close SEQ;$in0 = '/tmp/gb/'.$tmpfile;
    }

    $in0 = new G::IO($in0,'no msg');
    require G::Seq::Codon;    my $scaler = G::Seq::Codon::S_value($in0,%param);

    return SOAP::Data->type('string')->value($scaler);
}
