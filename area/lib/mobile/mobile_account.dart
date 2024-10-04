import 'package:flutter/foundation.dart';
import 'package:flutter/material.dart';
import '../shared/service_box.dart';
import 'mobile_nav_bar.dart';

class Service {
  final String name;
  final String logoPath;
  final bool isConnected;

  Service(this.name, this.logoPath, this.isConnected);
}

class MobileAccount extends StatelessWidget {
  const MobileAccount({super.key});

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
        title: const Text('Dashboard'),
        automaticallyImplyLeading: false,
      ),
      body: Column(
        children: [
          // Top 1/4 of the screen for account info
          Container(
            padding: const EdgeInsets.all(20.0),
            height: MediaQuery.of(context).size.height / 4,
            width: double.infinity,
            child: Column(
              mainAxisAlignment: MainAxisAlignment.center,
              children: const [
                CircleAvatar(
                  radius: 50,
                  backgroundImage: AssetImage('assets/images/profile.png'),
                ),
                SizedBox(height: 10),
                Text(
                  'John Doe',
                  style: TextStyle(
                    fontSize: 24,
                    fontWeight: FontWeight.bold,
                  ),
                ),
                Text(
                  'john.doe@example.com',
                  style: TextStyle(
                    fontSize: 16,
                    color: Colors.grey,
                  ),
                ),
              ],
            ),
          ),
          // Bottom 3/4 of the screen for API connection buttons
          Expanded(
            child: ListView.builder(
              padding: const EdgeInsets.all(20.0),
              itemCount: services.length,
              itemBuilder: (context, index) {
                final service = services[index];
                return Card(
                  margin: const EdgeInsets.symmetric(vertical: 15.0), // Reduced vertical margin
                  child: Center(
                    child: Container(
                      constraints: const BoxConstraints(
                        maxHeight: 60, // Set a maximum height for the buttons
                      ),
                      child: ServiceBox(
                        logoPath: service.logoPath,
                        isConnected: service.isConnected,
                        serviceName: service.name,
                        onConnect: () => handleConnect(service.name),
                      ),
                    ),
                  ),
                );
              },
            ),
          ),
        ],
      ),
      bottomNavigationBar: const MobileNavBar(),
    );
  }
}