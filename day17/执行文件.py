import settings
import logging.config

logging.config.dictConfig(settings.LOGGING_DIC)  # 导入上面定义的logging配置

logger1=logging.getLogger('logger1')

logger1.debug('调试日志')
