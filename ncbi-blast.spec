Name:                ncbi-blast
Version:             2.12.0
Release:             1
Summary:             NCBI BLAST finds regions of similarity between biological sequences.
License:             Public Domain
URL:                 https://blast.ncbi.nlm.nih.gov/Blast.cgi
Source0:             https://ftp.ncbi.nlm.nih.gov/blast/executables/blast+/2.12.0/ncbi-blast-2.12.0+-src.tar.gz
BuildRequires:       lmdb lmdb-devel
%description
The NCBI Basic Local Alignment Search Tool (BLAST) finds regions of
local similarity between sequences. The program compares nucleotide or
protein sequences to sequence databases and calculates the statistical
significance of matches. BLAST can be used to infer functional and
evolutionary relationships between sequences as well as help identify
members of gene families.

%prep
%autosetup -n %{name}-%{version}+-src -p1

%build
cd c++
export CFLAGS="%{build_cflags}"
export CXXFLAGS="%{build_cxxflags}"
export LDFLAGS="%{build_ldflags}"
./configure
cd ReleaseMT/build
sed -i "s/-fPIC/-fPIC -g/g" Makefile.mk
%make_build all_r

%install
install -d %{buildroot}%{_bindir}
install -d %{buildroot}%{_includedir}/ncbi-blast
install -d %{buildroot}%{_libdir}/ncbi-blast
rm -rf c++/ReleaseMT/bin/windowmasker_2.2.22_adapter.py
install -m 0755 c++/ReleaseMT/bin/* %{buildroot}%{_bindir}/
cp -r c++/ReleaseMT/inc/* %{buildroot}%{_includedir}/ncbi-blast
cp c++/ReleaseMT/lib/* %{buildroot}%{_libdir}/ncbi-blast/

%files
%defattr(-,root,root)
%_bindir/*
%{_includedir}/ncbi-blast/*
%{_libdir}/ncbi-blast/*

%changelog
* Wed Jul 28 2021 huanghaitao <huanghaitao8@huawei.com> - 2.12.0-1
- package init
