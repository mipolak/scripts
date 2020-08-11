#!/usr/bin/perl -p
# anonymize part of number starting on position 59 in all lines starting with ^3300
s{(?<=^3300)(.{59})((\d{6})(\d+)(\d{4}))}{
  $prefix = $1;
  $cc = $2;
  $bin = $3;
  $pan_mask = $4;
  $pan_visi = $5;
  $stars = length($pan_mask);
  $prefix . $bin .  ("*" x $stars) . $pan_visi
}exgms;
