window.initMap = function () {
    const map = new google.maps.Map(document.getElementById("map"), {
        center: { lat: 20, lng: 0 },
        zoom: 1.5,
        styles: [
            {
                stylers: [
                    {
                        color: "#ffffff",
                    },
                ],
            },
            {
                elementType: "geometry",
                stylers: [
                    {
                        color: "#ffffff",
                    },
                ],
            },
            {
                elementType: "geometry.fill",
                stylers: [
                    {
                        color: "#ffffff",
                    },
                ],
            },
            {
                elementType: "geometry.stroke",
                stylers: [
                    {
                        color: "#ffffff",
                    },
                ],
            },
            {
                featureType: "administrative",
                stylers: [
                    {
                        color: "#ffffff",
                    },
                ],
            },
            {
                featureType: "administrative",
                elementType: "geometry.fill",
                stylers: [
                    {
                        color: "#ffffff",
                    },
                ],
            },
            {
                featureType: "administrative",
                elementType: "labels.text.fill",
                stylers: [
                    {
                        color: "#1d0090",
                    },
                ],
            },
            {
                featureType: "administrative",
                elementType: "labels.text.stroke",
                stylers: [
                    {
                        color: "#ffe500",
                    },
                    {
                        weight: 8,
                    },
                ],
            },
            {
                featureType: "administrative.land_parcel",
                stylers: [
                    {
                        visibility: "off",
                    },
                ],
            },
            {
                featureType: "administrative.neighborhood",
                stylers: [
                    {
                        visibility: "off",
                    },
                ],
            },
            {
                featureType: "landscape",
                stylers: [
                    {
                        color: "#ffffff",
                    },
                ],
            },
            {
                featureType: "poi",
                stylers: [
                    {
                        color: "#ffffff",
                    },
                ],
            },
            {
                featureType: "road",
                stylers: [
                    {
                        color: "#ffffff",
                    },
                ],
            },
            {
                featureType: "transit",
                stylers: [
                    {
                        color: "#ffffff",
                    },
                ],
            },
            {
                featureType: "water",
                stylers: [
                    {
                        color: "#1d0090",
                    },
                ],
            },
            {
                featureType: "water",
                elementType: "labels.text",
                stylers: [
                    {
                        visibility: "off",
                    },
                ],
            },
        ],
    });

    var myIcon = new google.maps.MarkerImage(
        "/media/total.png",
        null,
        null,
        null,
        new google.maps.Size(100, 100)
    );

    const japan = [
        {
            label: "도쿄",
            name: "도쿄",
            lat: 35.5020581,
            lng: 138.4504777,
            icon: myIcon,
        },
        {
            label: "오사카",
            name: "오사카",
            lat: 34.6775704,
            lng: 135.403636,
            icon: myIcon,
        },
        {
            label: "삿포로",
            name: "삿포로",
            lat: 42.9848631,
            lng: 140.9183286,
            icon: myIcon,
        },
        {
            label: "후쿠오카",
            name: "후쿠오카",
            lat: 33.6495358,
            lng: 129.9343191,
            icon: myIcon,
        },
    ];

    japan.forEach(({ label, name, lat, lng, icon }) => {
        const marker = new google.maps.Marker({
            position: { lat, lng },
            label,
            map,
            icon,
        });
    });

    const france = [
        {
            label: "파리",
            name: "파리",
            lat: 48.8588255,
            lng: 2.2646345,
            icon: myIcon,
        },
        {
            label: "니스",
            name: "니스",
            lat: 43.7031657,
            lng: 7.1704111,
            icon: myIcon,
        },
        {
            label: "마르세유",
            name: "마르세유",
            lat: 43.280227,
            lng: 5.2158399,
            icon: myIcon,
        },
    ];

    france.forEach(({ label, name, lat, lng, icon }) => {
        const marker = new google.maps.Marker({
            position: { lat, lng },
            label,
            map,
            icon,
        });
    });
};
