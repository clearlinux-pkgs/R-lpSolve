#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-lpSolve
Version  : 5.6.13
Release  : 11
URL      : https://cran.r-project.org/src/contrib/lpSolve_5.6.13.tar.gz
Source0  : https://cran.r-project.org/src/contrib/lpSolve_5.6.13.tar.gz
Summary  : Interface to 'Lp_solve' v. 5.5 to Solve Linear/Integer Programs
Group    : Development/Tools
License  : LGPL-2.0
Requires: R-lpSolve-lib
BuildRequires : clr-R-helpers

%description
solving linear, integer and mixed integer programs. In this
        implementation we supply a "wrapper" function in C and some R
        functions that solve general linear/integer problems,
        assignment problems, and transportation problems. This version
        calls lp_solve version 5.5.

%package lib
Summary: lib components for the R-lpSolve package.
Group: Libraries

%description lib
lib components for the R-lpSolve package.


%prep
%setup -q -c -n lpSolve

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1523314655

%install
rm -rf %{buildroot}
export SOURCE_DATE_EPOCH=1523314655
export LANG=C
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=haswell -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library lpSolve
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=skylake-avx512 -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library lpSolve
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library lpSolve
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc -l %{buildroot}/usr/lib64/R/library lpSolve|| : 
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/lpSolve/DESCRIPTION
/usr/lib64/R/library/lpSolve/INDEX
/usr/lib64/R/library/lpSolve/Meta/Rd.rds
/usr/lib64/R/library/lpSolve/Meta/features.rds
/usr/lib64/R/library/lpSolve/Meta/hsearch.rds
/usr/lib64/R/library/lpSolve/Meta/links.rds
/usr/lib64/R/library/lpSolve/Meta/nsInfo.rds
/usr/lib64/R/library/lpSolve/Meta/package.rds
/usr/lib64/R/library/lpSolve/NAMESPACE
/usr/lib64/R/library/lpSolve/R/lpSolve
/usr/lib64/R/library/lpSolve/R/lpSolve.rdb
/usr/lib64/R/library/lpSolve/R/lpSolve.rdx
/usr/lib64/R/library/lpSolve/help/AnIndex
/usr/lib64/R/library/lpSolve/help/aliases.rds
/usr/lib64/R/library/lpSolve/help/lpSolve.rdb
/usr/lib64/R/library/lpSolve/help/lpSolve.rdx
/usr/lib64/R/library/lpSolve/help/paths.rds
/usr/lib64/R/library/lpSolve/html/00Index.html
/usr/lib64/R/library/lpSolve/html/R.css
/usr/lib64/R/library/lpSolve/libs/symbols.rds

%files lib
%defattr(-,root,root,-)
/usr/lib64/R/library/lpSolve/libs/lpSolve.so
/usr/lib64/R/library/lpSolve/libs/lpSolve.so.avx2
/usr/lib64/R/library/lpSolve/libs/lpSolve.so.avx512
