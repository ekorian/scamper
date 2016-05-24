# Scamper Tools

Scamper is a scalable, efficient, and feature-rich Internet packet
prober from CAIDA (http://www.caida.org/tools/measurement/scamper/).

Scamper is written in C and stores data in a binary "warts" format.

These tools attempt to replicate the functionality of scamper's
utilities by providing native python implementations.

* sc_warts.py:         warts file processing library
* sc_wartsdump.py:     parse binary warts files
* sc_sample.py:        sample python using warts class
