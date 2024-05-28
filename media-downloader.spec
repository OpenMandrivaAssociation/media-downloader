Name:           media-downloader
Version:        4.7.0
Release:        1
Summary:        Media Downloader is a Qt/C++ front end to yt-dlp, youtube-dl, gallery-dl, lux, you-get, svtplay-dl, aria2c, wget and safari books.. 
License:        GPL-2.0-or-later
URL:            https://github.com/mhogomchungu/media-downloader
Source0:       https://github.com/mhogomchungu/media-downloader/archive/refs/tags/%{version}/%{name}-%{version}.tar.gz
BuildSystem:	cmake
BuildOption: -DBUILD_WITH_QT6=ON
BuildRequires:  cmake
BuildRequires:  cmake(Qt6Core)
BuildRequires:  cmake(Qt6Network)
BuildRequires:  cmake(Qt6Widgets)
BuildRequires:  desktop-file-utils
Requires: yt-dlp
Requires: aria2

%description
This project is a Qt/C++ based GUI frontend to CLI multiple CLI based tools that
deal with downloading online media.
yt-dlp CLI tool is the default supported tool and other tools can be added by
downloading their extension and a list of supported extensions is managed here.

Features offered:-
 1. The GUI can be used to download any media from any website supported by
    installed extensions.
 2. The GUI offers a configurable list of preset options that can be used to
     download media if they are provided in multiple formats.
 3. The GUI offers an ability to do unlimited number of parallel downloads.
    Be careful with this ability because doing too many parallel downloads may
    cause the host to ban you.
 4. The GUI offers an ability to do batch downloads by entering individual link
    in the UI or telling the app to read them from a local file.
 5. The GUI offers an ability to download playlist from websites that supports
    them like youtube.
 6. The GUI offers ability to manage links to playlist to easily monitor their
    activities(subscriptions).
 7. The GUI is offered in multiple languages and as of this writing, the
    supported languages are English, Chinese, Spanish, Polish, Turkish, Russian,
    Japanese, French and Italian.

#find_lang %{name} --all-name --with-qt

%files -f %{name}.lang
%doc README.md
%license LICENSE
%{_bindir}/%{name}
%dir %{_datadir}/%{name}/
%dir %{_datadir}/%{name}/translations/
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/%{name}.png
