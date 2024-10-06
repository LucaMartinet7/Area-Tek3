import 'package:flutter/foundation.dart';
import 'package:flutter/material.dart';
import '../shared/service_box.dart';
import 'web_nav_bar.dart'; // Import the new WebNavBar

class Service {
  final String name;
  final String logoPath;
  final bool isConnected;

  Service(this.name, this.logoPath, this.isConnected);
}

class WebDashboard extends StatelessWidget {
  const WebDashboard({super.key});

  @override
  Widget build(BuildContext context) {
    final services = [
      Service('Spotify', 'assets/images/spotify.png', true),
      Service('Twitch', 'assets/images/twitch.png', false),
      Service('Google', 'assets/images/google.png', true),
      Service('Deezer', 'assets/images/deezer.png', false),
      Service('Microsoft', 'assets/images/microsoft.png', true),
    ];

    void handleConnect(String serviceName) {
      if (kDebugMode) {
        print('Connecting to $serviceName');
      }
    }

    return Scaffold(
      appBar: const WebNavBar(), // Use the WebNavBar
      body: Center(
        child: Padding(
          padding: const EdgeInsets.all(16.0),
          child: Row(
            crossAxisAlignment: CrossAxisAlignment.start,
            children: [
              _buildProfile(),
              const SizedBox(width: 16),
              _buildServiceBoxes(services, handleConnect),
            ],
          ),
        ),
      ),
    );
  }

  Widget _buildProfile() {
    return Expanded(
      flex: 1,
      child: Container(
        padding: const EdgeInsets.all(16.0),
        decoration: _boxDecoration(),
        child: Column(
          mainAxisAlignment: MainAxisAlignment.center,
          children: [
            const CircleAvatar(
              radius: 50,
              backgroundImage: AssetImage('assets/images/profile.png'),
            ),
            const SizedBox(height: 10),
            const Text(
              'John Doe',
              style: TextStyle(fontSize: 24, fontWeight: FontWeight.bold),
            ),
            const SizedBox(height: 5),
            const Text(
              'john.doe@example.com',
              style: TextStyle(fontSize: 16, color: Colors.grey),
            ),
          ],
        ),
      ),
    );
  }

  Widget _buildServiceBoxes(
      List<Service> services, void Function(String) handleConnect) {
    return Expanded(
      flex: 1,
      child: Column(
        mainAxisAlignment: MainAxisAlignment.spaceEvenly,
        children: services
            .map((service) => ServiceBox(
                  logoPath: service.logoPath,
                  isConnected: service.isConnected,
                  onConnect: () => handleConnect(service.name),
                  serviceName: service.name, // Pass the service name
                ))
            .toList(),
      ),
    );
  }

  BoxDecoration _boxDecoration() {
    return BoxDecoration(
      color: Colors.white,
      borderRadius: BorderRadius.circular(10),
      boxShadow: [
        BoxShadow(
          color: Colors.grey.withOpacity(0.5),
          spreadRadius: 2,
          blurRadius: 5,
          offset: const Offset(0, 3),
        ),
      ],
    );
  }
}