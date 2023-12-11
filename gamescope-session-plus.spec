Name:           gamescope-session-plus
Version:        {{{ git_dir_version }}}
Release:        1%{?dist}
Summary:        Gamescope session plus based on Valve's gamescope

License:        MIT
URL:            https://github.com/KyleGospo/gamescope-session

VCS:            {{{ git_dir_vcs }}}
Source:        	{{{ git_dir_pack }}}
BuildArch:      noarch

Requires:       gamescope
Requires:       python3

BuildRequires:  systemd-rpm-macros

%description
Gamescope session plus based on Valve's gamescope

# Disable debug packages
%define debug_package %{nil}

%prep
{{{ git_dir_setup_macro }}}

%build

%install
mkdir -p %{buildroot}%{_bindir}/
mkdir -p %{buildroot}%{_datadir}/
mkdir -p %{buildroot}%{_userunitdir}/
cp -rv usr/bin/* %{buildroot}%{_bindir}
cp -rv usr/share/* %{buildroot}%{_datadir}
cp -v usr/lib/systemd/user/* %{buildroot}%{_userunitdir}

# Do post-installation
%post

# Do before uninstallation
%preun

# Do after uninstallation
%postun

# This lists all the files that are included in the rpm package and that
# are going to be installed into target system where the rpm is installed.
%files
%license LICENSE
%doc README.md
%{_bindir}/export-gpu
%{_bindir}/gamescope-session-plus
%{_datadir}/gamescope-session-plus/device-quirks
%{_datadir}/gamescope-session-plus/gamescope-session-plus
%{_userunitdir}/gamescope-session-plus@.service

# Finally, changes from the latest release of your application are generated from
# your project's Git history. It will be empty until you make first annotated Git tag.
%changelog
{{{ git_dir_changelog }}}
