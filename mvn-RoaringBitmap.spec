#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : mvn-RoaringBitmap
Version  : 0.5.11
Release  : 2
URL      : https://github.com/RoaringBitmap/RoaringBitmap/archive/RoaringBitmap-0.5.11.tar.gz
Source0  : https://github.com/RoaringBitmap/RoaringBitmap/archive/RoaringBitmap-0.5.11.tar.gz
Source1  : https://repo1.maven.org/maven2/org/roaringbitmap/RoaringBitmap/0.5.11/RoaringBitmap-0.5.11.jar
Source2  : https://repo1.maven.org/maven2/org/roaringbitmap/RoaringBitmap/0.5.11/RoaringBitmap-0.5.11.pom
Summary  : No detailed summary available
Group    : Development/Tools
License  : Apache-2.0
Requires: mvn-RoaringBitmap-data = %{version}-%{release}

%description
Real data sets for bitmap testing
packaged by Daniel Lemire on April 3rd 2014
Essentially, each file represents a set of integer values. You can create
bitmaps out of these files.

%package data
Summary: data components for the mvn-RoaringBitmap package.
Group: Data

%description data
data components for the mvn-RoaringBitmap package.


%prep

%build

%install
mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/roaringbitmap/RoaringBitmap/0.5.11
cp %{SOURCE1} %{buildroot}/usr/share/java/.m2/repository/org/roaringbitmap/RoaringBitmap/0.5.11

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/roaringbitmap/RoaringBitmap/0.5.11
cp %{SOURCE2} %{buildroot}/usr/share/java/.m2/repository/org/roaringbitmap/RoaringBitmap/0.5.11


%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/share/java/.m2/repository/org/roaringbitmap/RoaringBitmap/0.5.11/RoaringBitmap-0.5.11.jar
/usr/share/java/.m2/repository/org/roaringbitmap/RoaringBitmap/0.5.11/RoaringBitmap-0.5.11.pom
