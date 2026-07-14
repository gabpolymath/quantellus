import os
import json
import time
import numpy as np
import yfinance as yf
import tifffile
from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from src.translations import TRANSLATIONS

app = FastAPI()

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_ROOT = os.path.dirname(BASE_DIR)

app.mount("/static", StaticFiles(directory=os.path.join(BASE_DIR, "static")), name="static")
app.mount("/data", StaticFiles(directory=os.path.join(PROJECT_ROOT, "data")), name="data")

templates = Jinja2Templates(directory=os.path.join(BASE_DIR, "templates"))

# cache
FINANCIAL_CACHE = {}
CACHE_TTL_SECONDS = 1800

COMMODITIES = {
    "grano": {
        "dict_key": "comm_grano",
        "ticker": "ZW=F",
        "exchange": "CBOT",
        "pivot_historico": 0.35,
        "regions": [
            {
                "name_key": "region_wheat_1",
                "ndvi_default": 0.46,
                "image": "visual/wheat_ndvi_lat46.68_lng30.66.jpg",
                "tiff": "raw/wheat_ndvi_lat46.68_lng30.66.tiff",
                "coords": "46.68, 30.66",
                "date": "2025-06-20"
            },
            {
                "name_key": "region_wheat_2",
                "ndvi_default": 0.31,
                "image": "visual/wheat_ndvi_lat48.50_lng-102.01.jpg",
                "tiff": "raw/wheat_ndvi_lat48.50_lng-102.01.tiff",
                "coords": "48.50, -102.01",
                "date": "2025-07-09"
            }
        ]
    },
    "mais": {
        "dict_key": "comm_mais",
        "ticker": "ZC=F",
        "exchange": "CBOT",
        "pivot_historico": 0.32,
        "regions": [
            {
                "name_key": "region_corn_1",
                "ndvi_default": 0.25,
                "image": "visual/corn_ndvi_lat41.41_lng-93.28.jpg",
                "tiff": "raw/corn_ndvi_lat41.41_lng-93.28.tiff",
                "coords": "41.41, -93.28",
                "date": "2025-07-14"
            },
            {
                "name_key": "region_corn_2",
                "ndvi_default": 0.32,
                "image": "visual/corn_ndvi_lat39.17_lng-86.46.jpg",
                "tiff": "raw/corn_ndvi_lat39.17_lng-86.46.tiff",
                "coords": "39.17, -86.46",
                "date": "2025-07-05"
            }
        ]
    },
    "soia": {
        "dict_key": "comm_soia",
        "ticker": "ZS=F",
        "exchange": "CBOT",
        "pivot_historico": 0.35,
        "regions": [
            {
                "name_key": "region_soy_1",
                "ndvi_default": 0.51,
                "image": "visual/soybeans_ndvi_lat-12.63_lng-56.20.jpg",
                "tiff": "raw/soybeans_ndvi_lat-12.63_lng-56.20.tiff",
                "coords": "-12.63, -56.20",
                "date": "2025-02-09"
            },
            {
                "name_key": "region_soy_2",
                "ndvi_default": 0.25,
                "image": "visual/soybeans_ndvi_lat-33.85_lng-60.74.jpg",
                "tiff": "raw/soybeans_ndvi_lat-33.85_lng-60.74.tiff",
                "coords": "-33.85, -60.74",
                "date": "2025-02-19"
            }
        ]
    }
}

def get_cached_financial_data(ticker: str, lang: str):
    t = TRANSLATIONS[lang]
    now = time.time()
    
    if ticker in FINANCIAL_CACHE:
        cached_time, cached_data = FINANCIAL_CACHE[ticker]
        if now - cached_time < CACHE_TTL_SECONDS:
            print(t["log_cache_hit"].format(ticker=ticker))
            return cached_data
            
    print(t["log_cache_miss"].format(ticker=ticker))
    
    try:
        yf_ticker = yf.Ticker(ticker)
        hist = yf_ticker.history(start="2025-01-01", timeout=5)
        
        if hist.empty:
            return None
            
        current_price = float(hist["Close"].iloc[-1])
        raw_volume = int(hist["Volume"].iloc[-1])
        
        if raw_volume >= 1_000_000:
            current_volume_str = f"{raw_volume / 1_000_000:.2f} M"
        elif raw_volume >= 1_000:
            current_volume_str = f"{raw_volume / 1_000:.1f} K"
        else:
            current_volume_str = str(raw_volume)
            
        daily_change_str = "N/A" if lang == "en" else "N/D"
        change_color = "var(--text-muted)"
        
        if len(hist) >= 2:
            prev_price = float(hist["Close"].iloc[-2])
            price_diff = current_price - prev_price
            pct_change = (price_diff / prev_price) * 100
            
            sign = "+" if price_diff > 0 else ""
            daily_change_str = f"{sign}{price_diff:.2f} ({sign}{pct_change:.2f}%)"
            
            if price_diff > 0:
                change_color = "var(--success)"
            elif price_diff < 0:
                change_color = "var(--danger)"
                
        chart_data = []
        for index, row in hist.iterrows():
            chart_data.append({
                "date": index.strftime('%Y-%m-%d'),
                "open": round(float(row["Open"]), 2),
                "high": round(float(row["High"]), 2),
                "low": round(float(row["Low"]), 2),
                "close": round(float(row["Close"]), 2)
            })
            
        data_to_cache = {
            "price": round(current_price, 2),
            "volume": current_volume_str,
            "daily_change_str": daily_change_str,
            "change_color": change_color,
            "chart_data_json": json.dumps(chart_data)
        }
        
        FINANCIAL_CACHE[ticker] = (now, data_to_cache)
        return data_to_cache

    except Exception as e:
        print(t["log_fin_error"].format(ticker=ticker, error=e))
        return None

@app.get("/", response_class=HTMLResponse)
def home(request: Request, lang: str = "en"):
    if lang not in TRANSLATIONS:
        lang = "en"
    t = TRANSLATIONS[lang]
    
    return templates.TemplateResponse(
        request=request, 
        name="index.html", 
        context={"result": None, "error": None, "commodities": COMMODITIES, "t": t, "lang": lang}
    )


@app.post("/", response_class=HTMLResponse)
def analyze(request: Request, commodity_key: str = Form(""), lang: str = Form("en")):
    if lang not in TRANSLATIONS:
        lang = "en"
    t = TRANSLATIONS[lang]

    try:
        if not commodity_key or commodity_key not in COMMODITIES:
            raise ValueError(t["err_invalid_commodity"])
        
        comm = COMMODITIES[commodity_key]
        ticker = comm["ticker"]
        regions = comm["regions"]
        
        computed_ndvis = []
        for r in regions:
            tiff_path = os.path.join(PROJECT_ROOT, "data", r["tiff"])
            try:
                ndvi_matrix = tifffile.imread(tiff_path)
                
                if len(ndvi_matrix.shape) > 2:
                    ndvi_matrix = ndvi_matrix[0]
                
                valori_validi = ndvi_matrix[~np.isnan(ndvi_matrix) & (ndvi_matrix >= -1.0) & (ndvi_matrix <= 1.0)]
                
                if valori_validi.size > 0:
                    real_ndvi = float(np.mean(valori_validi))
                else:
                    raise ValueError(t["err_ndvi_invalid"])
                
                r["ndvi"] = round(real_ndvi, 2)
            except Exception as e:
                r["ndvi"] = r.get("ndvi_default", 0.0)
                print(t["log_tiff_warning"].format(tiff_path=tiff_path, error=e))
            
            computed_ndvis.append(r["ndvi"])
            
        avg_ndvi = sum(computed_ndvis) / len(computed_ndvis) if computed_ndvis else 0.0
        
        fin_data = get_cached_financial_data(ticker, lang)
        
        if fin_data:
            price = fin_data["price"]
            volume = fin_data["volume"]
            daily_change_str = fin_data["daily_change_str"]
            change_color = fin_data["change_color"]
            chart_data_json = fin_data["chart_data_json"]
        else:
            na_fallback = "N/A" if lang == "en" else "N/D"
            price = na_fallback
            volume = na_fallback
            daily_change_str = na_fallback
            change_color = "var(--text-muted)"
            chart_data_json = "[]"

        asset_pivot = comm.get("pivot_historico", 0.35)

        if avg_ndvi < asset_pivot:
            signal = "BUY"
            status = t["status_buy"]
            motivation = t["mot_buy"].format(ticker=ticker)
            color_class = "signal-buy"
        else:
            signal = "SELL"
            status = t["status_sell"]
            motivation = t["mot_sell"].format(ticker=ticker)
            color_class = "signal-sell"
        
        result = {
            "selected_key": commodity_key,
            "ticker": ticker,
            "exchange": comm.get("exchange", "CBOT"),
            "avg_ndvi": round(avg_ndvi, 2),
            "price": price,
            "volume": volume,
            "daily_change_str": daily_change_str,
            "change_color": change_color,         
            "signal": signal,
            "status": status,
            "motivation": motivation,
            "color_class": color_class,
            "regions": regions,
            "chart_data_json": chart_data_json
        }
        
        return templates.TemplateResponse(
            request=request, 
            name="index.html", 
            context={"result": result, "error": None, "commodities": COMMODITIES, "t": t, "lang": lang}
        )
        
    except Exception as e:
        return templates.TemplateResponse(
            request=request,
            name="index.html",
            context={"result": None, "error": f"{t['error_log']}: {str(e)}", "commodities": COMMODITIES, "t": t, "lang": lang}
        )