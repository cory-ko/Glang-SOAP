# G-language SOAP Service (version 1.0.1)

All rights reserved. Copyright © 2012 by OSHITA Kazuki

## License

This Service is free software; you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either or version 2 of the License. See also [GNU General Public License Version 2][GPL].

## About
G-language Genome Analysis Environment (G-language GAE) is a set of Perl libraries for genome sequence analysis that is compatible with BioPerl, equipped with several software interfaces (interactive Perl/UNIX shell with persistent data, AJAX Web GUI, Perl API). The software package contains more than 100 original analysis programs especially focusing on bacterial genome analysis, including those for the identification of binding sites with information theory, analysis of nucleotide composition bias, analysis of the distribution of characteristic oligonucleotides, analysis of codons and prediction of expression levels, and visualization of genomic information. Taking advantage of the [BioHackathon 2009][BioHackathon2], we have recently developed REST/SOAP web service APIs for this software system, in order to provide higher interoperability with other programming languages and bioinformatics software tools.

SOAP interface provides language-independent access to more than 100 analysis programs. The WSDL file contains descriptions for all available programs in a single file, and can be readily loaded in Taverna 2 workbench to integrate with other services to construct workflows. Example workflows are available at the [myExperiment](http://www.myexperiment.org) website.

## Project page
[http://soap.g-language.org/](http://soap.g-language.org/)

## WSDL file
[http://soap.g-language.org/g-language.wsdl](http://soap.g-language.org/g-language.wsdl)

## List of available processes
- [BioCatalogue web site](http://www.biocatalogue.org/services/2623-glangsoapservice_651637#overview)
- [AJAX Document Center](http://ws.g-language.org/gdoc/)
  - List of functions as well as available options

## Publication
"G-language genome analysis environment with REST and SOAP web service interfaces", Arakawa K, Kido N, Oshita K, Tomita M, *Nucleic Acids Res.*, 2010, 38 Suppl:W700-705 ([PubMed](http://www.ncbi.nlm.nih.gov/pubmed/20439313)).

## Requirements
- [G-language GAE][G-language] (version 1.8.13)
- [SOAP::Lite][SOAP::Lite] (version 0.712)

## Usage
Users are able to connect to this service via SOAP 1.1 (RPC/Encoded)

### Perl (SOAP::Lite 0.60)
    use SOAP::Lite;
    use strict;
 
    my $soap = SOAP::Lite->service("http://soap.g-language.org/g-language.wsdl");
    my $in0   = SOAP::Data->new(name=>'in0',value=>"ecoli");
 
    my %param = (-cumulative=>1);
    my $inputParams = SOAP::Data->name('params')->type(map=>¥%param);
 
    print $soap->gcskew($in0, $inputParams);

### Ruby
    require 'soap/wsdlDriver'
 
    wsdl = "http://soap.g-language.org/g-language.wsdl"
    serv = SOAP::WSDLDriverFactory.new(wsdl).create_rpc_driver
    serv.generate_explicit_type = true
 
    hash = {"-cumulative" => 1}
    print serv.gcskew("ecoli",hash)

### Python
    from SOAPpy import WSDL
 
    wsdl = 'http://soap.g-language.org/g-language.wsdl'
    serv = WSDL.Proxy(wsdl)
 
    param = {"cumulative" : 1}
    print serv.gcskew('ecoli',param)

## Contact
Kazuki Oshita <cory@g-language.org>  
  Institute for Advanced Biosciences, Keio University.

[BioHackathon2]:http://hackathon2.dbcls.jp)
[GPL]:http://www.gnu.org/licenses/gpl-2.0.html
[G-language]:http://www.g-language.org/
[SOAP::Lite]:http://search.cpan.org/~mkutter/SOAP-Lite-0.712/lib/SOAP/Lite.pm
