"""
Command Line Interface pentru BebeConn
"""

import argparse
import sys
from .core import BebeConn
from .server import BebeServer
from .agent import BebeAgent

def main():
    """Funcția principală pentru CLI."""
    parser = argparse.ArgumentParser(
        description="BebeConn - Monitorizare Laptop de la Distanță",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Exemple de utilizare:
  bebe-conn start                    # Pornește totul local
  bebe-conn start --ngrok           # Pornește cu ngrok pentru acces extern
  bebe-conn start --port 8080       # Pornește pe portul 8080
  bebe-conn start --screenshot 60   # Screenshot la fiecare 60 secunde
  bebe-conn server                  # Pornește doar serverul
  bebe-conn agent                   # Pornește doar agentul
        """
    )
    
    subparsers = parser.add_subparsers(dest='command', help='Comenzi disponibile')
    
    # Comanda start
    start_parser = subparsers.add_parser('start', help='Pornește sistemul complet')
    start_parser.add_argument('--ngrok', action='store_true', 
                            help='Folosește ngrok pentru acces extern')
    start_parser.add_argument('--port', type=int, default=5000,
                            help='Portul pentru server (default: 5000)')
    start_parser.add_argument('--screenshot', type=int, default=120,
                            help='Intervalul pentru screenshot-uri în secunde (default: 120)')
    
    # Comanda server
    server_parser = subparsers.add_parser('server', help='Pornește doar serverul')
    server_parser.add_argument('--port', type=int, default=5000,
                             help='Portul pentru server (default: 5000)')
    
    # Comanda agent
    agent_parser = subparsers.add_parser('agent', help='Pornește doar agentul')
    agent_parser.add_argument('--server-url', default='http://localhost:5000',
                            help='URL-ul serverului (default: http://localhost:5000)')
    agent_parser.add_argument('--screenshot', type=int, default=120,
                            help='Intervalul pentru screenshot-uri în secunde (default: 120)')
    
    args = parser.parse_args()
    
    if not args.command:
        parser.print_help()
        return
    
    try:
        if args.command == 'start':
            print("🚀 BebeConn - Pornire sistem complet...")
            bebe = BebeConn(
                ngrok=args.ngrok,
                port=args.port,
                screenshot_interval=args.screenshot
            )
            bebe.start()
            
        elif args.command == 'server':
            print("📡 BebeConn - Pornire server...")
            server = BebeServer(port=args.port)
            server.start()
            
        elif args.command == 'agent':
            print("🤖 BebeConn - Pornire agent...")
            agent = BebeAgent(
                server_url=args.server_url,
                screenshot_interval=args.screenshot
            )
            agent.start()
            
    except KeyboardInterrupt:
        print("\n⏹️  Oprire...")
        sys.exit(0)
    except Exception as e:
        print(f"❌ Eroare: {e}")
        sys.exit(1)

if __name__ == '__main__':
    main()
