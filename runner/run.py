import logging

logger = logging.getLogger(__name__)


def run_playbook(playbook, inventory, runner):
    logger.info("Entering run_playbook")
    try:
        result = runner.run(playbook)
    except Exception:
        logger.error("playbook failed id=%s", playbook.id, exc_info=True)
        raise
    logger.info("playbook finished id=%s rc=%s", playbook.id, result.rc)
    logger.info("Exiting run_playbook")
    return result
