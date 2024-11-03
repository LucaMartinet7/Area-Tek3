import 'package:flutter/material.dart';
import '../shared/exit_button.dart';

class WebNavBar extends StatelessWidget implements PreferredSizeWidget {
  const WebNavBar({super.key});

  @override
  Widget build(BuildContext context) {
    final services = [
      {'asset': 'assets/vectors/account.png', 'route': '/dashboard', 'isConnected': true},
      {'asset': 'assets/vectors/spotify.png', 'route': '/spotify', 'isConnected': true},
      {'asset': 'assets/vectors/twitch.png', 'route': '/twitch', 'isConnected': true},
      {'asset': 'assets/vectors/google.png', 'route': '/google', 'isConnected': true},
      {'asset': 'assets/vectors/youtube.png', 'route': '/youtube', 'isConnected': true},
      {'asset': 'assets/vectors/gmail.png', 'route': '/gmail', 'isConnected': true},
    ];

    final connectedServices = services.where((service) => service['isConnected'] as bool).toList();
    final currentRoute = ModalRoute.of(context)?.settings.name;

    return Container(
      decoration: BoxDecoration(
        border: Border.all(
          color: const Color.fromARGB(255, 140, 211, 255),
          width: 5,
        ),
      ),
      child: AppBar(
        backgroundColor: Colors.transparent,
        elevation: 0,
        leading: buildExitButton(context),
        flexibleSpace: Row(
          children: <Widget>[
            Expanded(
              child: Row(
                mainAxisAlignment: MainAxisAlignment.center,
                children: connectedServices.map((service) {
                  return _buildNavButton(
                    context,
                    service['asset'] as String,
                    service['route'] as String,
                    service['isConnected'] as bool,
                    currentRoute == service['route'],
                  );
                }).toList(),
              ),
            ),
            _buildNavButton(context, 'assets/vectors/info.png', '/about', true, currentRoute == '/about'),
          ],
        ),
      ),
    );
  }

  Widget _buildNavButton(BuildContext context, String assetPath, String route, bool isConnected, bool isCurrentPage) {
    return IconButton(
      onPressed: isConnected && ModalRoute.of(context)?.settings.name != route
          ? () => Navigator.pushNamed(context, route)
          : null,
      icon: Image.asset(
        assetPath,
        width: 32,
        height: 32,
        color: isCurrentPage
            ? Colors.blue
            : isConnected
                ? const Color.fromARGB(255, 140, 211, 255)
                : Colors.grey,
      ),
    );
  }

  @override
  Size get preferredSize => const Size.fromHeight(kToolbarHeight);
}