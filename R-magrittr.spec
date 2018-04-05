#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-magrittr
Version  : 1.5
Release  : 40
URL      : http://cran.r-project.org/src/contrib/magrittr_1.5.tar.gz
Source0  : http://cran.r-project.org/src/contrib/magrittr_1.5.tar.gz
Summary  : A Forward-Pipe Operator for R
Group    : Development/Tools
License  : MIT
Requires: R-mime
BuildRequires : R-knitr
BuildRequires : R-mime
BuildRequires : R-testthat
BuildRequires : clr-R-helpers

%description
new forward-pipe operator, %>%. This operator will forward a
    value, or the result of an expression, into the next function
    call/expression. There is flexible support for the type
    of right-hand side expressions. For more information, see
    package vignette.
    To quote Rene Magritte, "Ceci n'est pas un pipe."

%prep
%setup -q -c -n magrittr

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1502408311

%install
rm -rf %{buildroot}
export SOURCE_DATE_EPOCH=1502408311
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
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library magrittr
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library magrittr
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc -l %{buildroot}/usr/lib64/R/library magrittr
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/magrittr/DESCRIPTION
/usr/lib64/R/library/magrittr/INDEX
/usr/lib64/R/library/magrittr/LICENSE
/usr/lib64/R/library/magrittr/Meta/Rd.rds
/usr/lib64/R/library/magrittr/Meta/features.rds
/usr/lib64/R/library/magrittr/Meta/hsearch.rds
/usr/lib64/R/library/magrittr/Meta/links.rds
/usr/lib64/R/library/magrittr/Meta/nsInfo.rds
/usr/lib64/R/library/magrittr/Meta/package.rds
/usr/lib64/R/library/magrittr/Meta/vignette.rds
/usr/lib64/R/library/magrittr/NAMESPACE
/usr/lib64/R/library/magrittr/R/magrittr
/usr/lib64/R/library/magrittr/R/magrittr.rdb
/usr/lib64/R/library/magrittr/R/magrittr.rdx
/usr/lib64/R/library/magrittr/doc/index.html
/usr/lib64/R/library/magrittr/doc/magrittr.R
/usr/lib64/R/library/magrittr/doc/magrittr.Rmd
/usr/lib64/R/library/magrittr/doc/magrittr.html
/usr/lib64/R/library/magrittr/help/AnIndex
/usr/lib64/R/library/magrittr/help/aliases.rds
/usr/lib64/R/library/magrittr/help/magrittr.rdb
/usr/lib64/R/library/magrittr/help/magrittr.rdx
/usr/lib64/R/library/magrittr/help/paths.rds
/usr/lib64/R/library/magrittr/html/00Index.html
/usr/lib64/R/library/magrittr/html/R.css
