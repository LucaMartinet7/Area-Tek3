import 'package:flutter/foundation.dart';
import 'package:flutter/material.dart';
import '../shared/service_name_box.dart';
import 'mobile_nav_bar.dart';

class Service {
  final String name;
  final String logoPath;
  final bool isConnected;
  final String route;

  Service(this.name, this.logoPath, this.isConnected, this.route);
}

class MobileDashboard extends StatelessWidget {
  const MobileDashboard({super.key});

  @override
  Widget build(BuildContext context) {
    final services = [
      Service('Spotify', 'assets/images/spotify.png', true, '/spotify'),
      Service('Twitch', 'assets/images/twitch.png', false, '/twitch'),
      Service('Google', 'assets/images/google.png', true, '/google'),
      Service('Youtube', 'assets/vectors/youtube.png', false, '/youtube'),
      Service('Microsoft', 'assets/images/microsoft.png', true, '/microsoft'),
    ];

    void handleConnect(BuildContext context, String route) {
      if (kDebugMode) {
        print('Connecting to $route');
      }
      Navigator.pushNamed(context, route);
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
                      onConnect: () => handleConnect(context, service.route),
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