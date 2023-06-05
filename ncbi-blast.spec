Name:                ncbi-blast
Version:             2.14.0
Release:             1
Summary:             NCBI BLAST finds regions of similarity between biological sequences.
License:             Public Domain
URL:                 https://blast.ncbi.nlm.nih.gov/Blast.cgi
Source0:             https://ftp.ncbi.nlm.nih.gov/blast/executables/blast+/LATEST/ncbi-blast-%{version}+-src.tar.gz
%ifarch riscv64
Patch0:              add-riscv-support.patch
%endif
Requires:	     glibc perl python3  pcre elfutils-libelf zlib lmdbzstd lzo libuv libnghttp2 sqlite
BuildRequires:       gcc-c++ make cpio zlib-devel  lmdb-devel
%description
The NCBI Basic Local Alignment Search Tool (BLAST) finds regions of
local similarity between sequences. The program compares nucleotide or
protein sequences to sequence databases and calculates the statistical
significance of matches. BLAST can be used to infer functional and
evolutionary relationships between sequences as well as help identify
members of gene families.

%prep
%autosetup -n %{name}-%{version}+-src -p1
%ifarch loongarch64
%_update_config_guess
%_update_config_sub
%endif

%build
cd c++
export CFLAGS="%{build_cflags}"
export CXXFLAGS="%{build_cxxflags}"
export LDFLAGS="%{build_ldflags}"
./configure  --prefix=/usr --with-dll --with-mt
cd ReleaseMT/build
sed -i "s/-fPIC/-fPIC -g/g" Makefile.mk
%make_build all_r

%install
cd c++
install -d -m 0755 %{buildroot}%{_bindir}
install -d -m 0755 %{buildroot}%{_includedir}/ncbi-tools++
install -d -m 0755 %{buildroot}%{_libdir}/
rm -rf ReleaseMT/bin/windowmasker_2.2.22_adapter.py
install -m 0755 ReleaseMT/bin/* %{buildroot}%{_bindir}/
cp -r ReleaseMT/inc/* %{buildroot}%{_includedir}/ncbi-tools++
cp -r ReleaseMT/lib/* %{buildroot}%{_libdir}/

%files
%defattr(-,root,root)
%_bindir/*
%{_includedir}/ncbi-tools++/*
%{_libdir}/*

%changelog
* Fri Jul 2 2023 guoyizhang <kuoi@bioarchlinux.org> - 2.14.0-1
- update to 2.14.0

* Wed May 31 2023 huajingyun <huajingyun@loongson.cn> - 2.12.0-4
- update config.guess and config.sub for loongarch64

* Thu Nov 24 2022 misaka00251 <liuxin@iscas.ac.cn> - 2.12.0-3
- Add riscv support

* Tue Feb 15 2022 herengui <herengui@uniontech.com> - 2.12.0-2
- add missing buildrquires.

* Wed Jul 28 2021 huanghaitao <huanghaitao8@huawei.com> - 2.12.0-1
- package init
