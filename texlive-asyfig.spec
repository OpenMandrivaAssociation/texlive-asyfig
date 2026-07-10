%global tl_name asyfig
%global tl_revision 17512

Name:		texlive-%{tl_name}
Epoch:		1
Version:	0.1c
Release:	%{tl_revision}.1
Summary:	Commands for using Asymptote figures
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/asyfig
License:	lppl
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/asyfig.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/asyfig.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/asyfig.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
Requires(pre):	texlive-tlpkg
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package provides a means of reading Asymptote figures from separate
files, rather than within the document, as is standard in the asymptote
package, which is provided as part of the Asymptote bundle. The
asymptote way can prove cumbersome in a large document; the present
package allows the user to process one picture at a time, in simple test
documents, and then to migrate (with no fuss) to their use in the target
document.

%prep
%setup -q -c -a1 -a2
rm -rf tlpkg
if [ -d RELOC ]; then
	cp -a RELOC/. .
	rm -rf RELOC
fi

%build

%install
mkdir -p %{buildroot}%{_datadir}/texmf-dist
# Flat tlnet layout: tex/ doc/ source/ fonts/ ... -> texmf-dist/
if [ -d texmf-dist ]; then
	cp -a texmf-dist/. %{buildroot}%{_datadir}/texmf-dist/
elif [ -d texmf ]; then
	mkdir -p %{buildroot}%{_datadir}/texmf
	cp -a texmf/. %{buildroot}%{_datadir}/texmf/
else
	for d in * .[!.]* ..?*; do
		[ -e "$d" ] || continue
		case "$d" in tlpkg|RELOC) continue ;; esac
		cp -a "$d" %{buildroot}%{_datadir}/texmf-dist/
	done
fi
rm -rf %{buildroot}%{_datadir}/texmf-dist/tlpkg

%files
%dir %{_datadir}/texmf-dist
%dir %{_datadir}/texmf-dist/doc
%dir %{_datadir}/texmf-dist/source
%dir %{_datadir}/texmf-dist/tex
%dir %{_datadir}/texmf-dist/doc/latex
%dir %{_datadir}/texmf-dist/source/latex
%dir %{_datadir}/texmf-dist/tex/latex
%dir %{_datadir}/texmf-dist/doc/latex/asyfig
%dir %{_datadir}/texmf-dist/source/latex/asyfig
%dir %{_datadir}/texmf-dist/tex/latex/asyfig
%dir %{_datadir}/texmf-dist/doc/latex/asyfig/example
%doc %{_datadir}/texmf-dist/doc/latex/asyfig/README
%doc %{_datadir}/texmf-dist/doc/latex/asyfig/asyfig.pdf
%doc %{_datadir}/texmf-dist/doc/latex/asyfig/example/frf.asy
%doc %{_datadir}/texmf-dist/doc/latex/asyfig/example/test-asyfig.tex
%doc %{_datadir}/texmf-dist/source/latex/asyfig/asyfig.ins
%doc %{_datadir}/texmf-dist/source/latex/asyfig/asyfig.tex
%{_datadir}/texmf-dist/tex/latex/asyfig/asyalign.sty
%{_datadir}/texmf-dist/tex/latex/asyfig/asyfig.sty
%{_datadir}/texmf-dist/tex/latex/asyfig/asyprocess.sty
