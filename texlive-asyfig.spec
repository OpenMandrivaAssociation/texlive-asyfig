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
BuildSystem:	texlive
BuildRequires:	texlive-tlpkg
%texlive_base_requires
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package provides a means of reading Asymptote figures from separate
files, rather than within the document, as is standard in the asymptote
package, which is provided as part of the Asymptote bundle. The
asymptote way can prove cumbersome in a large document; the present
package allows the user to process one picture at a time, in simple test
documents, and then to migrate (with no fuss) to their use in the target
document.

