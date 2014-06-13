# revision 17512
# category Package
# catalog-ctan /macros/latex/contrib/asyfig
# catalog-date 2010-03-20 11:11:38 +0100
# catalog-license lppl
# catalog-version 0.1c
Name:		texlive-asyfig
Version:	0.1c
Release:	7
Summary:	Commands for using Asymptote figures
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/asyfig
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/asyfig.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/asyfig.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/asyfig.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package provides a means of reading Asymptote figures from
separate files, rather than within the document, as is standard
in the asymptote package, which is provided as part of the
Asymptote bundle. The asymptote way can prove cumbersome in a
large document; the present package allows the user to process
one picture at a time, in simple test documents, and then to
migrate (with no fuss) to their use in the target document.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/asyfig/asyalign.sty
%{_texmfdistdir}/tex/latex/asyfig/asyfig.sty
%{_texmfdistdir}/tex/latex/asyfig/asyprocess.sty
%doc %{_texmfdistdir}/doc/latex/asyfig/README
%doc %{_texmfdistdir}/doc/latex/asyfig/asyfig.pdf
%doc %{_texmfdistdir}/doc/latex/asyfig/example/frf.asy
%doc %{_texmfdistdir}/doc/latex/asyfig/example/test-asyfig.tex
#- source
%doc %{_texmfdistdir}/source/latex/asyfig/asyfig.ins
%doc %{_texmfdistdir}/source/latex/asyfig/asyfig.tex

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}


%changelog
* Tue Jan 03 2012 Paulo Andrade <pcpa@mandriva.com.br> 0.1c-2
+ Revision: 749367
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 0.1c-1
+ Revision: 717865
- texlive-asyfig
- texlive-asyfig
- texlive-asyfig
- texlive-asyfig
- texlive-asyfig

