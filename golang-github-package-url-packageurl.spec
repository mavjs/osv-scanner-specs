# Generated by go2rpm 1.9.0
%bcond_without check
%global debug_package %{nil}

# https://github.com/package-url/packageurl-go
%global goipath         github.com/package-url/packageurl-go
Version:                0.1.1

%gometa -f


%global common_description %{expand:
Go implementation of the package url spec.}

%global golicenses      LICENSE mit.LICENSE
%global godocs          README.md

Name:           %{goname}
Release:        %autorelease
Summary:        Go implementation of the package url spec

License:        MIT
URL:            %{gourl}
Source:         %{gosource}

%description %{common_description}

%gopkg

%prep
%goprep
%autopatch -p1

%generate_buildrequires
%go_generate_buildrequires

%install
%gopkginstall

%if %{with check}
%check
%gocheck
%endif

%gopkgfiles

%changelog
%autochangelog
