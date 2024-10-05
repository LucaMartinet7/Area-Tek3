import 'package:flutter/foundation.dart';
import 'package:flutter/material.dart';
import '../shared/service_name_box.dart'; // Import the new widget
import 'mobile_nav_bar.dart';

class Service {
  final String name;
  final String logoPath;
  final bool isConnected;

  Service(this.name, this.logoPath, this.isConnected);
}

class MobileDashboard extends StatelessWidget {
  const MobileDashboard({super.key});

  @override
  Widget build(BuildContext context) {
    final services = [
      Service('Spotify', 'assets/images/spotify.png', true),
      Service('Twitch', 'assets/images/twitch.png', false),
      Service('Google', 'assets/images/google.png', true),
      Service('YouTube', 'assets/images/deezer.png', false),
      Service('Microsoft', 'assets/images/microsoft.png', true),
    ];

void handleConnect(String serviceName) {
  if (kDebugMode) {
    print('Connecting to $serviceName');
  }
}

return Scaffold(
  appBar: AppBar(
    automaticallyImplyLeading: false,
  ),
  body: Center(
    child: SingleChildScrollView(
      child: Column(
        mainAxisAlignment: MainAxisAlignment.center,
        children: services.map((service) {
          return Center(
            child: Card(
              margin: const EdgeInsets.symmetric(vertical: 30.0), // Adjusted vertical margin
              child: Container(
                constraints: const BoxConstraints(
                  maxWidth: 400,
                  maxHeight: 80, // Set a maximum height for the buttons
                ),
                child: ServiceNameBox(
                  logoPath: service.logoPath,
                  serviceName: service.name,
                  onConnect: () => handleConnect(service.name),
                  borderColor: service.isConnected ? Colors.green : Colors.red, // Set border color based on connection status
                ),
              ),
            ),
          );
        }).toList(),
      ),
    ),
  ),
  bottomNavigationBar: const MobileNavBar(),
);
  }
}