Name:           webp-pixbuf-loader
Version:        0.0.4
Release:        1
Summary:        WebP image loader for GTK+ applications
License:        LGPLv2+
URL:            https://github.com/aruiz/webp-pixbuf-loader
Source0:        https://github.com/aruiz/%{name}/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires:  meson
BuildRequires:  pkgconfig(gdk-pixbuf-2.0)
BuildRequires:  pkgconfig(libwebp)

Requires:       gdk-pixbuf2.0%{?_isa}

%description
webp-pixbuf-loader contains a plugin to load WebP images in GTK+ applications

%prep
%autosetup

%build
%meson -Dgdk_pixbuf_query_loaders_path=gdk-pixbuf-query-loaders-%{__isa_bits}
%meson_build

%install
%meson_install

%files
%license LICENSE.LGPL-2
%{_libdir}/gdk-pixbuf-2.0/*/loaders/libpixbufloader-webp.so
%{_datadir}/thumbnailers/webp-pixbuf.thumbnailer
