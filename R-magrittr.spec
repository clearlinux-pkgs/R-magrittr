#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-magrittr
Version  : 1.5
Release  : 17
URL      : http://cran.r-project.org/src/contrib/magrittr_1.5.tar.gz
Source0  : http://cran.r-project.org/src/contrib/magrittr_1.5.tar.gz
Summary  : A Forward-Pipe Operator for R
Group    : Development/Tools
License  : MIT
BuildRequires : R-knitr
BuildRequires : clr-R-helpers

%description
magrittr -  Ceci n'est pas un pipe.
====================================
[![Build Status](https://travis-ci.org/smbache/magrittr.png?branch=dev)](https://travis-ci.org/smbache/magrittr)

%prep
%setup -q -c -n magrittr

%build

%install
rm -rf %{buildroot}
export LANG=C
mkdir -p %{buildroot}/usr/lib64/R/library
R CMD INSTALL --install-tests --build  -l %{buildroot}/usr/lib64/R/library magrittr
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=intel.com,localhost
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc -l %{buildroot}/usr/lib64/R/library magrittr


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/magrittr/DESCRIPTION
/usr/lib64/R/library/magrittr/INDEX
/usr/lib64/R/library/magrittr/LICENSE
/usr/lib64/R/library/magrittr/Meta/Rd.rds
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
