
Summary: Linux/PPC64 specific utilities
Name:    ppc64-utils
Version: 0.14
Release: 9%{?dist}

# La la la. There is nothing here any more.
License: GPLv2

Group:   System Environment/Base

BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
ExclusiveArch: ppc ppc64
Requires: yaboot
Requires: binutils
Requires: powerpc-utils kernel-bootwrapper lsvpd libvpd

%description
A collection of utilities for Linux on PPC64 platforms.

%prep

%build

%install

%clean

%files

%changelog
* Wed Feb 17 2010 Roman Rakus <rrakus@redhat.com> 0.14-9
- Removed every lines in all sections.

* Fri Jan 22 2010 Roman Rakus <rrakus@redhat.com> 0.14-8
- Added requires for lsvpd and libvpd
  Resolves: #463311

* Tue Jan 19 2010 Roman Rakus rrakus@redhat.com 0.14-7
- Don't require ps3-utils, we don't support it on RHEL
  Resolves: #547791
- Require yaboot at all

* Mon Nov 30 2009 Dennis Gregorovic <dgregor@redhat.com> - 0.14-6.1
- Rebuilt for RHEL 6

* Tue Nov 10 2009 Roman Rakus <rrakus@redhat.com> - 0.14-6
- Remove requires powerpc-utils-papr, since powerpc-utils provides it

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.14-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Feb 25 2009 Josh Boyer <jwboyer@gmail.com> - 0.14-4
- Change Requires to ps3-utils as the package was renamed

* Mon Jul  7 2008 Roman Rakus <rrakus@redhat.com> - 0.14-3
- Requires yaboot only for ppc arch

* Mon Feb 18 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 0.14-2
- Autorebuild for GCC 4.3

* Mon Dec  3 2007 David Woodhouse <dwmw2@redhat.com> 0.14-1
- Completely empty except for Requires: now. Yay!

* Wed Nov 28 2007 David Woodhouse <dwmw2@redhat.com> 0.13-1
- Remove powerpc-utils, powerpc-utils-papr, ps3pf-utils

* Tue Oct 23 2007 Jeremy Katz <katzj@redhat.com> - 0.12-3
- and one more file is needed

* Sun Oct 14 2007 Jeremy Katz <katzj@redhat.com> - 0.12-2
- add files needed for creating bootable cds

* Sat Sep 15 2007 David Cantrell <dcantrell@redhat.com> - 0.12-1
- Upgraded to powerpc-utils-1.0.6 and powerpc-utils-papr-1.0.4
- Updated license tag to reflect licenses of all included components

* Mon Aug 27 2007 David Cantrell <dcantrell@redhat.com> - 0.11-5
- Spec file style cleanup
- BR dtc now for ps3.dtb since Core/Extras merge is complete
- BR kernel-devel
- Pass kernel include path for ps3pf_utils-1.0.9 build

* Mon Apr 16 2007 David Woodhouse <dwmw2@redhat.com> - 0.11-4
- Fix handling of PS3 secondary PPU in bootwrapper

* Sun Apr  8 2007 David Woodhouse <dwmw2@redhat.com> - 0.11-3
- Update kernel bootwrapper magic

* Sat Mar 31 2007 David Woodhouse <dwmw2@redhat.com> - 0.11-2
- Include ps3pf_utils.

* Mon Oct 30 2006 Paul Nasrat <pnasrat@redhat.com> - 0.11-1
- Update powerpc-utils to 1.0.3 (#212181)

* Mon Oct 16 2006 Paul Nasrat <pnasrat@redhat.com> - 0.10-1
- Include powerpc-utils and powerpc-utils-papr (#184685)

* Sun Oct 01 2006 Jesse Keating <jkeating@redhat.com> - 0.9-15
- rebuilt for unwind info generation, broken in gcc-4.1.1-21

* Thu Sep 21 2006 Peter Jones <pjones@redhat.com> - 0.9-14
- Fix iSeries support in addRamDisk

* Fri Jul 14 2006 Jesse Keating <jkeating@redhat.com> - 0.9-13
- rebuild

* Fri Feb 10 2006 Jesse Keating <jkeating@redhat.com> - 0.9-12.2.1
- bump again for double-long bug on ppc(64)

* Tue Feb 07 2006 Jesse Keating <jkeating@redhat.com> - 0.9-12.2
- rebuilt for new gcc4.1 snapshot and glibc changes

* Fri Dec 09 2005 Jesse Keating <jkeating@redhat.com>
- rebuilt

* Fri Nov 18 2005 David Woodhouse <dwmw2@redhat.com> - 0.9-12
- Update zImage.stub from 2.6.15-rc1 kernel
- Link zImage at 3MiB since the POWER5 doesn't like it at 8MiB

* Tue Oct 25 2005 Paul Nasrat <pnasrat@redhat.com> - 0.9-11
- Bump internal version above rhel4 ver
- Pull in later ppc64-utils (#169035)

* Tue Oct 25 2005 Paul Nasrat <pnasrat@redhat.com> - 0.7-13
- Stop scanning nvram on broken content (#170418)

* Tue Sep 27 2005 David Woodhouse <dwmw2@redhat.com> - 0.7-12
- Work around old Pegasos II 'claim' method bug

* Wed Sep 21 2005 David Woodhouse <dwmw2@redhat.com> - 0.7-11
- Build zImage.stub 32-bit even on ppc64

* Tue Sep 20 2005 David Woodhouse <dwmw2@redhat.com> - 0.7-10
- Include zImage stub, capable of both ppc32 and ppc64 boot.

* Tue Mar 15 2005 Paul Nasrat <pnasrat@redhat.com> - 0.7-9
- Rebuild 

* Wed Oct 20 2004 Jeremy Katz <katzj@redhat.com> - 0.7-8
- add some more error handling to new mkzimage

* Wed Oct 20 2004 Jeremy Katz <katzj@redhat.com> - 0.7-7
- New mkzimage script from dhowells that works with the zImage.stub in 
  our 2.6 kernels
  - use mktemp instead of predictable filenames in /tmp
  - use the zImage.lds in the package instead of output by the script

* Wed Sep 22 2004 Jeremy Katz <katzj@redhat.com> - 0.7-5
- rebuild

* Tue Jun 15 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Wed Mar  3 2004 Jeremy Katz <katzj@redhat.com> - 0.7-3
- rebuild

* Tue Nov  4 2003 Matt Wilson <msw@redhat.com> 0.7-2
- make clean before buildinig nvsetenv to nuke the old binary (#107943)

* Tue Sep 16 2003 Jeremy Katz <katzj@redhat.com> 0.7-1
- mkzimage bugfix

* Mon Aug 18 2003 Matt Wilson <msw@redhat.com> 0.6-1
- incorporate ppc64-utils 0.4 from IBM

* Mon Aug 11 2003 Matt Wilson <msw@redhat.com> 0.5-1
- add nvsetenv

* Wed Jul 30 2003 Matt Wilson <msw@redhat.com> 0.4-1
- add mkzimage for pSeries zImage creation with initrd

* Tue May 20 2003 Matt Wilson <msw@redhat.com> 0.3-1
- add addSystemMap from arch/ppc64/boot/addSystemMap.c

* Fri Apr 18 2003 Jeremy Katz <katzj@redhat.com> 0.2-1
- make addRamDisk quieter by default, set $VERBOSE to get old output

* Tue Apr 15 2003 Jeremy Katz <katzj@redhat.com> 0.1-1
- include addRamDisk from kernel source tree (arch/ppc64/boot/addRamDisk.c) 
  to create kernel/initrd blobs on iSeries


