Name:           webp-pixbuf-loader
Version:        0.2.5
Release:        1
Summary:        WebP image loader for GTK+ applications
License:        LGPLv2+
URL:            https://github.com/aruiz/webp-pixbuf-loader
Source0:        https://github.com/aruiz/%{name}/archive/%{version}/%{name}-%{version}.tar.gz
Patch0:        https://github.com/aruiz/webp-pixbuf-loader/commit/834657c8d189b6b0354401a00a842f539d7c29e4.patch

BuildRequires:  meson
BuildRequires:  pkgconfig(gdk-pixbuf-2.0)
BuildRequires:  pkgconfig(libwebp)

Requires:       gdk-pixbuf2.0%{?_isa}

%description
webp-pixbuf-loader contains a plugin to load WebP images in GTK+ applications

%prep
%autosetup -p1

%build
%meson -Dgdk_pixbuf_query_loaders_path=gdk-pixbuf-query-loaders-%{__isa_bits}
%meson_build

%install
%meson_install

%files
%license LICENSE.LGPL-2
%{_libdir}/gdk-pixbuf-2.0/*/loaders/libpixbufloader-webp.so
%{_datadir}/thumbnailers/webp-pixbuf.thumbnailer
