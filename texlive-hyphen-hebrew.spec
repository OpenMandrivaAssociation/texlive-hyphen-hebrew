%global tl_name hyphen-hebrew
%global tl_revision 74032

Name:		texlive-%{tl_name}
Version:	%{tl_revision}
Release:	2
Summary:	Hebrew hyphenation patterns.
Group:		Publishing
URL:		https://www.ctan.org/pkg/hyphen-hebrew
License:	LPPL
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/hyphen-hebrew.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Requires:	texlive(hyph-utf8)
Requires:	texlive(hyphen-base)
Requires:	texlive-tlpkg
Provides:	texlive(%{tl_name}) = %{version}

%description
Prevents hyphenation in Arabic.


%install -a
mkdir -p %{buildroot}%{_texmf_language_dat_d}
cat > %{buildroot}%{_texmf_language_dat_d}/%{tl_name} <<'TL_HYPHEN_EOF'
% from hyphen-hebrew:
hebrew hyph-he.tex
TL_HYPHEN_EOF
mkdir -p %{buildroot}%{_texmf_language_def_d}
cat > %{buildroot}%{_texmf_language_def_d}/%{tl_name} <<'TL_HYPHEN_EOF'
% from hyphen-hebrew:
\addlanguage{hebrew}{hyph-he.tex}{}{0}{0}
TL_HYPHEN_EOF
mkdir -p %{buildroot}%{_texmf_language_lua_d}
cat > %{buildroot}%{_texmf_language_lua_d}/%{tl_name} <<'TL_HYPHEN_EOF'
-- from hyphen-hebrew:
['hebrew'] = {
	loader = 'hyph-he.tex',
	lefthyphenmin = 0,
	righthyphenmin = 0,
	synonyms = {  },
},
TL_HYPHEN_EOF
