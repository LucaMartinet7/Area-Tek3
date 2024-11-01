import 'package:flutter/foundation.dart';
import 'package:flutter/material.dart';
import '../shared/service_name_box.dart';
import 'mobile_nav_bar.dart';

class Service {
  final String logoPath;
  final bool isConnected;
  final String route;
  final List<Color> colors;

  Service(this.logoPath, this.isConnected, this.route, this.colors);
}

class MobileDashboard extends StatelessWidget {
  const MobileDashboard({super.key});

  @override
  Widget build(BuildContext context) {
    final services = [
      Service('assets/vectors/spotify.png', true, '/spotify', [const Color(0xFF1DB954)]),
      Service('assets/vectors/twitch.png', false, '/twitch', [const Color(0xFF9146FF)]),
      Service('assets/vectors/google.png', true, '/google', [Colors.blue, Colors.red, Colors.yellow, Colors.green]),
      Service('assets/vectors/youtube.png', false, '/youtube', [const Color(0xFFFF0000)]),
      Service('assets/vectors/microsoft.png', true, '/microsoft', [Colors.blue, Colors.green, Colors.yellow, Colors.red]),
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
                  margin: const EdgeInsets.symmetric(vertical: 30.0),
                  child: Container(
                    constraints: const BoxConstraints(
                      maxWidth: 400,
                      maxHeight: 80,
                    ),
                    child: GestureDetector(
                      onTap: service.isConnected ? () => handleConnect(context, service.route) : null,
                      child: ServiceNameBox(
                        logoPath: service.logoPath,
                        onConnect: () => handleConnect(context, service.route),
                        backgroundColors: service.isConnected ? service.colors : [Colors.grey],
                      ),
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