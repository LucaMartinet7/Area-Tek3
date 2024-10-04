import 'dart:io' show Platform;

bool isMobile() {
  return Platform.isAndroid || Platform.isIOS; // ios for later implementation

}