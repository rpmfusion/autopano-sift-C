Summary: SIFT feature detection
Name: autopano-sift-C
Version: 2.4.1
Release: 0.4.20080220svn%{?dist}
License: GPLv2
Group: Applications/Multimedia
# The source for this package was pulled from upstream's vcs.  Use the
# following commands to generate the tarball:
#  svn export -r 2904 https://hugin.svn.sourceforge.net/svnroot/hugin/autopano-sift-C/trunk autopano-sift-C
#  cd autopano-sift-C
#  cmake . && make package_source
Source: %{name}-%{version}.tar.gz
Source1: autopano-sift-C.README.fedora
URL: http://hugin.sourceforge.net/
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildRequires: libpano13-devel libxml2-devel cmake

%description
This package provides an implementation of the SIFT algorithm and a set of
utilities to utilize the algorithm to match two or more images.  The output is
created as project file for the hugin panorama stitching software.

%prep
%setup -q

%build
cp -a %{SOURCE1} README.fedora
%cmake .
make VERBOSE=1 %{?_smp_mflags}

%install
rm -rf %{buildroot}
make install DESTDIR=%{buildroot}

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%doc README LICENSE README.1ST README.fedora
%{_bindir}/autopano
%{_bindir}/autopano-sift-c
%{_bindir}/generatekeys
%{_bindir}/autopano-c-complete.sh
%{_mandir}/man1/autopano.1.gz
%{_mandir}/man1/generatekeys.1.gz
%{_mandir}/man1/autopano-c-complete.1.gz
%{_mandir}/man7/autopano-sift-c.7.gz

%changelog
* Sat Oct 10 2009 Thorsten Leemhuis <fedora [AT] leemhuis [DOT] info> - 2.4.1-0.4.20080220svn
- rebuilt

* Sun Mar 29 2009 Thorsten Leemhuis <fedora [AT] leemhuis [DOT] info> - 2.4.1-0.3.20080220svn
- rebuild for new F11 features

* Sun Aug 03 2008 Thorsten Leemhuis <fedora [AT] leemhuis [DOT] info - 2.4.1-0.2.20080220svn
- rebuild

* Wed Feb 20 2008 Bruno Postle <bruno@postle.net> 2.4.1-0.1.20080220svn
  - update from SVN, 2.4.1 pre-release
  - new cmake build system, new tool autopano-sift-c

* Sat Jan 19 2008 Bruno Postle <bruno@postle.net> 2.4-5.20080102svn
  - put README.fedora on SOURCES, change post-release versioning slightly

* Mon Jan 14 2008 Bruno Postle <bruno@postle.net> 2.4-4.1.20080102svn
  - update with review fixes

* Wed Jan 02 2008 Bruno Postle <bruno@postle.net> 2.4-4svn20080102
  - update from SVN Revision: 2597
  - switch pano12 dependency to pano13

* Thu Nov 15 2007 Bruno Postle <bruno@postle.net> 2.4-3
  - fix license tag
  - bugfix from http://sourceforge.net/tracker/index.php?func=detail&aid=1808333&group_id=77506&atid=550441

* Mon Jul 02 2007 Bruno Postle <bruno@postle.net> 2.4-2
  - add autopano-c-complete.sh

* Tue Feb 19 2007 Bruno Postle <bruno@postle.net> 2.4-1
  - initial rpm

