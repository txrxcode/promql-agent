import argparse
import pprint
import sys
from pathlib import Path
from dotenv import load_dotenv

# Make backend/app importable when running from repo root without install
ROOT = Path(__file__).parent
BACKEND = ROOT / "backend"
if BACKEND.exists() and str(BACKEND) not in sys.path:
    sys.path.insert(0, str(BACKEND))

load_dotenv(ROOT / ".env.local")

from app.agents.sre_agent import SREAgent  # noqa: E402


def get_agent(agent_name: str):
    agents = {
        "sre_agent": SREAgent,
        "sre": SREAgent,
        "promql": SREAgent,
    }
    key = agent_name.lower()
    if key not in agents:
        raise ValueError(
            f"Unknown agent '{agent_name}'. Available: {', '.join(agents)}"
        )
    return agents[key]()


def main():
    parser = argparse.ArgumentParser(
        prog="promql-agent",
        description="CLI agent for Prometheus, Loki, and Grafana",
    )
    parser.add_argument("-q", "--question", type=str, help="Question to ask the agent.")
    parser.add_argument("-a", "--agent", type=str, default="sre_agent",
                        help="Agent name (default: sre_agent).")
    parser.add_argument("--incident", type=str, nargs=2,
                        metavar=("ALERT_NAME", "SEVERITY"),
                        help="Trigger incident response. e.g. --incident HighCPU critical")
    parser.add_argument("--health", action="store_true", help="System health report.")
    parser.add_argument("--demo", action="store_true", help="Run tools demo.")
    parser.add_argument("--tools-health", action="store_true",
                        help="Check tool connectivity.")

    args = parser.parse_args()
    pp = pprint.PrettyPrinter(indent=2, width=80)

    try:
        agent = get_agent(args.agent)

        if args.demo:
            print("🎬 Running tools demo...")
            from app.tools.sre_tools import demo_sre_tools
            demo_sre_tools()
            return

        if args.tools_health:
            print("🔧 Checking tool health...")
            pp.pprint(agent.tools.health_check())
            return

        if args.health:
            print("🏥 Generating system health report...")
            response = agent.get_system_health()
        elif args.incident:
            alert_name, severity = args.incident
            print(f"🚨 Incident response: {alert_name} ({severity})")
            response = agent.execute_incident_response(alert_name, severity)
        elif args.question:
            print(f"❓ {args.question}")
            response = agent.ask_question(args.question)
        else:
            parser.print_help()
            return

        print(f"\n🤖 Agent: {args.agent}")
        print("📋 Response:")
        pp.pprint(response)

    except Exception as e:
        print(f"❌ Error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
