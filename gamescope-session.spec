Name:           gamescope-session
Version:        {{{ git_dir_version }}}
Release:        1%{?dist}
Summary:        Steam Big Picture Mode/Gamemode session based on gamescope

License:        MIT
URL:            https://github.com/KyleGospo/gamescope-session

VCS:            {{{ git_dir_vcs }}}
Source:        	{{{ git_dir_pack }}}
Patch0:			fedora.patch
BuildArch:      noarch

Requires:       gamescope
Requires:       python3

BuildRequires:  systemd-rpm-macros

%description
Steam Big Picture Mode/Gamemode session based on gamescope

# Disable debug packages
%define debug_package %{nil}

%prep
{{{ git_dir_setup_macro }}}
%patch 0 -p1

%build

%install
mkdir -p %{buildroot}%{_bindir}/
mkdir -p %{buildroot}%{_datadir}/
mkdir -p %{buildroot}%{_userunitdir}/
cp -rv usr/bin/* %{buildroot}%{_bindir}
cp -rv usr/share/* %{buildroot}%{_datadir}
cp -v usr/lib/systemd/user/* %{buildroot}%{_userunitdir}
rm -rf %{buildroot}%{_bindir}/steamos-polkit-helpers
rm %{buildroot}%{_bindir}/jupiter-biosupdate
rm %{buildroot}%{_bindir}/steamos-session-select
rm %{buildroot}%{_bindir}/steamos-update

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
%{_bindir}/gamescope-session
%{_bindir}/steam-http-loader
%{_bindir}/export-gpu
%{_bindir}/steamos-select-branch
%{_datadir}/applications/gamescope-mimeapps.list
%{_datadir}/applications/steam_http_loader.desktop
%{_datadir}/gamescope-session/device-quirks
%{_datadir}/gamescope-session/gamescope-session-script
%{_datadir}/polkit-1/actions/org.chimeraos.update.policy
%{_datadir}/wayland-sessions/gamescope-session.desktop
%{_userunitdir}/gamescope-session.service

# Finally, changes from the latest release of your application are generated from
# your project's Git history. It will be empty until you make first annotated Git tag.
%changelog
{{{ git_dir_changelog }}}
